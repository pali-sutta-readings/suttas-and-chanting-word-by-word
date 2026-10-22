#!/usr/bin/env bash
# Test scripts/migrate-legacy.sh against the legacy snapshots, writing into a
# temporary directory. Skips (exit 0) when the legacy folder is not present,
# e.g. on a fresh clone on another machine.
#
# Usage: tests/test_migrate.sh [LEGACY_DIR]

set -euo pipefail

repo=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
migrate=$repo/scripts/migrate-legacy.sh
legacy=${1:-$HOME/prods/sites/pali-sutta-readings-project/suttas-and-chanting-word-by-word_docs}

if [[ ! -d $legacy ]]; then
    echo "test_migrate: SKIP (no legacy folder at $legacy)"
    exit 0
fi

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
dest=$tmp/repo
failures=0

check() {
    local what=$1 got=$2 want=$3
    if [[ $got == "$want" ]]; then
        echo "ok   $what"
    else
        echo "FAIL $what: got '$got', want '$want'"
        failures=$((failures + 1))
    fi
}

# run NAME ARGS…: run the migration into $dest, log to $tmp/NAME.log, and
# set $status to its exit code.
run() {
    local name=$1
    shift
    status=0
    "$migrate" --dest "$dest" "$@" "$legacy" >"$tmp/$name.log" 2>&1 || status=$?
}

# First run: everything is copied.
run run1
check "first run exits 0" $status 0

manifest=$dest/sources/MIGRATION-MANIFEST.tsv
check "texts in texts/" "$(find "$dest/texts" -name '[0-9]*.md' | wc -l)" 209
check "changelogs in texts/" "$(find "$dest/texts" -name CHANGELOG.md | wc -l)" 17
check "originals in sources/originals/" "$(find "$dest/sources/originals" -type f | wc -l)" 6
check "no originals in texts/" "$(find "$dest/texts" -name '00_original_*' | wc -l)" 0
check "no macOS junk" "$(find "$dest" -name '._*' -o -name .DS_Store | wc -l)" 0
check "manifest header" "$(head -1 "$manifest")" \
    $'dest\tsnapshot\tsource\tsha256\tdiffers_from_final\tchanged_lines_vs_final'
check "texts differing from FINAL" \
    "$(awk -F'\t' '$5 == "yes" && $1 ~ /\/[0-9][^\/]*\.md$/' "$manifest" | wc -l)" 48
check "changelogs differing from FINAL" \
    "$(awk -F'\t' '$5 == "yes" && $1 ~ /CHANGELOG\.md$/' "$manifest" | wc -l)" 9
check "01–08 texts come from S22" \
    "$(awk -F'\t' '$1 ~ /^texts\/0[1-8].*\/[0-9][^\/]*\.md$/ && $2 != "S22"' "$manifest" | wc -l)" 0
check "a manifest sha256 is right" \
    "$(awk -F'\t' '$1 == "texts/07a_suttas/CHANGELOG.md" {print $4}' "$manifest")" \
    "$(sha256sum <"$dest/texts/07a_suttas/CHANGELOG.md" | cut -d' ' -f1)"

# Second run: a no-op.
before=$(cd "$dest" && find . -type f -exec sha256sum {} + | sort)
run run2
check "second run exits 0" $status 0
check "second run copies nothing" "$(grep -c '^  total: 0 copied' "$tmp/run2.log")" 1
check "second run changes no file" "$(cd "$dest" && find . -type f -exec sha256sum {} + | sort)" "$before"

# A modified destination file: refused without --force, replaced with it.
target=$dest/texts/01_morning_chanting/01_dedication_of_offerings.md
echo "local edit" >>"$target"
run run3
check "modified destination is refused" $status 1
check "refusal names the file" "$(grep -c 'texts/01_morning_chanting/01_dedication_of_offerings.md' "$tmp/run3.log")" 1
check "refused run leaves the edit" "$(tail -1 "$target")" "local edit"

run run4 --force
check "--force run exits 0" $status 0
check "--force restores the file" "$(cd "$dest" && find . -type f -exec sha256sum {} + | sort)" "$before"

if ((failures)); then
    echo "test_migrate: $failures failure(s)"
    exit 1
fi
echo "test_migrate: all checks passed"
