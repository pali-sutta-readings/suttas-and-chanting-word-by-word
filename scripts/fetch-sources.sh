#!/usr/bin/env bash
# Clone or update the upstream source repos listed in sources/UPSTREAM.txt
# into sources/upstream/<name>/, checked out at each block's pinned commit.
#
# With --update, check out the head of each block's branch instead and write
# that commit back into UPSTREAM.txt. Location-only sources are never
# downloaded; their URLs are printed.

set -euo pipefail

usage() {
    cat <<'EOF'
Usage: scripts/fetch-sources.sh [--update]

Clone or update sources/upstream/ at the commits pinned in sources/UPSTREAM.txt.

Options:
  --update    check out the head of each branch and re-pin UPSTREAM.txt
  -h, --help  show this help
EOF
}

UPDATE=0
while (($#)); do
    case $1 in
        --update) UPDATE=1; shift ;;
        -h | --help) usage; exit 0 ;;
        *) usage >&2; exit 2 ;;
    esac
done

repo=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
upstream_txt=$repo/sources/UPSTREAM.txt
upstream_dir=$repo/sources/upstream

[[ -f $upstream_txt ]] || { echo "fetch-sources: missing $upstream_txt" >&2; exit 2; }

# One `|`-separated line per block: name, type, url, branch, commit, and the
# location URLs (url, epub, index) for location-only blocks.
read_blocks() {
    awk '
        function flush() {
            if (b["name"] != "")
                print b["name"] "|" b["type"] "|" b["url"] "|" b["branch"] "|" b["commit"] "|" b["epub"] "|" b["index"]
            delete b
        }
        /^#/ { next }
        /^[[:space:]]*$/ { flush(); next }
        {
            key = $0; sub(/:.*/, "", key)
            val = $0; sub(/^[^:]*:[[:space:]]*/, "", val)
            b[key] = val
        }
        END { flush() }
    ' "$upstream_txt"
}

# set_commit NAME SHA: rewrite the commit line of block NAME in UPSTREAM.txt.
set_commit() {
    local tmp
    tmp=$(mktemp)
    awk -v name="$1" -v sha="$2" '
        /^name:/ { cur = $0; sub(/^name:[[:space:]]*/, "", cur) }
        /^[[:space:]]*$/ { cur = "" }
        cur == name && /^commit:/ { print "commit: " sha; next }
        { print }
    ' "$upstream_txt" >"$tmp"
    cat "$tmp" >"$upstream_txt"
    rm -f "$tmp"
}

# Read all blocks first: --update rewrites UPSTREAM.txt inside the loop.
mapfile -t blocks < <(read_blocks)

failed=0
mkdir -p "$upstream_dir"

for block in "${blocks[@]}"; do
    IFS="|" read -r name type url branch commit epub index <<<"$block"
    case $type in
        location-only)
            echo "$name: location only, not downloaded"
            for u in "$url" "$epub" "$index"; do
                [[ -n $u ]] && echo "  $u"
            done
            continue
            ;;
        git) ;;
        *)
            echo "$name: unknown type '$type'" >&2
            failed=1
            continue
            ;;
    esac

    dir=$upstream_dir/$name
    if [[ ! -d $dir/.git ]]; then
        echo "$name: cloning $url"
        git clone --quiet --filter=blob:none "$url" "$dir"
    fi

    if ((UPDATE)); then
        git -C "$dir" fetch --quiet origin "$branch"
        target=$(git -C "$dir" rev-parse FETCH_HEAD)
        if [[ $target != "$commit" ]]; then
            set_commit "$name" "$target"
            echo "$name: pinned $branch at ${target:0:12}${commit:+ (was ${commit:0:12})}"
        fi
    else
        if [[ -z $commit ]]; then
            echo "$name: no commit pinned in UPSTREAM.txt; run with --update" >&2
            failed=1
            continue
        fi
        target=$commit
        if ! git -C "$dir" cat-file -e "$target^{commit}" 2>/dev/null; then
            git -C "$dir" fetch --quiet origin "$branch"
        fi
        if ! git -C "$dir" cat-file -e "$target^{commit}" 2>/dev/null; then
            git -C "$dir" fetch --quiet origin "$target" || {
                echo "$name: pinned commit $target not found upstream" >&2
                failed=1
                continue
            }
        fi
    fi

    if [[ $(git -C "$dir" rev-parse -q --verify HEAD 2>/dev/null) == "$target" ]]; then
        echo "$name: up to date at ${target:0:12}"
    else
        git -C "$dir" -c advice.detachedHead=false checkout --quiet --detach "$target"
        echo "$name: checked out ${target:0:12}"
    fi
done

exit $failed
