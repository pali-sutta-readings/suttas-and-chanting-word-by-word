#!/usr/bin/env bash
# Copy the legacy project's texts and assets into this repo, byte for byte.
#
# Which snapshot each file comes from, and why, is set out in
# docs/legacy-migration.md. In short: texts for 01–08 come from S22, their
# changelogs from BACKUP, and everything for 09a–10 from FINAL. File
# timestamps are never used to choose a version.
#
# The script verifies the snapshots before copying anything, refuses to
# overwrite a destination file that differs from its source (unless --force),
# and writes sources/MIGRATION-MANIFEST.tsv with one row per file.

set -euo pipefail

usage() {
    cat <<'EOF'
Usage: scripts/migrate-legacy.sh [options] [LEGACY_DIR]

Copy the legacy texts and assets into this repo.

LEGACY_DIR defaults to
  ~/prods/sites/pali-sutta-readings-project/suttas-and-chanting-word-by-word_docs

Options:
  --dest DIR        destination repo root (default: this script's repo)
  --exercises DIR   pali-exercises checkout (default: LEGACY_DIR/../pali-exercises)
  --force           overwrite destination files that differ from their source
  --dry-run         verify and report, but write nothing
  -h, --help        show this help

Environment:
  NOTO_MATH         path to NotoSansMath-Regular.ttf
                    (default: /usr/share/fonts/noto/NotoSansMath-Regular.ttf)
EOF
}

die() {
    echo "migrate-legacy: $*" >&2
    exit 2
}

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

LEGACY=~/prods/sites/pali-sutta-readings-project/suttas-and-chanting-word-by-word_docs
DEST=$(dirname "$script_dir")
EXERCISES=
FORCE=0
DRY_RUN=0
NOTO_MATH=${NOTO_MATH:-/usr/share/fonts/noto/NotoSansMath-Regular.ttf}

while (($#)); do
    case $1 in
        --dest) DEST=${2:?--dest needs a directory}; shift 2 ;;
        --exercises) EXERCISES=${2:?--exercises needs a directory}; shift 2 ;;
        --force) FORCE=1; shift ;;
        --dry-run) DRY_RUN=1; shift ;;
        -h | --help) usage; exit 0 ;;
        -*) usage >&2; die "unknown option: $1" ;;
        *) LEGACY=$1; shift ;;
    esac
done

LEGACY=${LEGACY%/}
EXERCISES=${EXERCISES:-$(dirname "$LEGACY")/pali-exercises}
FINAL=$LEGACY/final-build-files/Pali-translations-formatted-md-files
S22=$FINAL/_build/s22src
BACKUP=$LEGACY/last-backup/Pali-translations-formatted-md-files

for d in "$LEGACY" "$FINAL" "$S22" "$BACKUP" "$EXERCISES"; do
    [[ -d $d ]] || die "missing directory: $d"
done
[[ -f $NOTO_MATH ]] || die "missing Noto Sans Math font: $NOTO_MATH (set NOTO_MATH, or install noto-fonts)"
mkdir -p "$DEST" 2>/dev/null || [[ $DRY_RUN == 1 ]] || die "cannot create $DEST"
DEST=$(cd "$DEST" 2>/dev/null && pwd || echo "$DEST")

# Expected totals in texts/ and sources/originals/.
EXPECT_TEXTS=209
EXPECT_CHANGELOGS=17
EXPECT_ORIGINALS=6

# macOS junk that is never copied.
is_junk() {
    local base=${1##*/}
    [[ $base == ._* || $base == .DS_Store || $base == *.pyc || $1 == */__pycache__/* ]]
}

# files_in DIR: set FILES to the files directly inside DIR, junk skipped.
# Junk is counted once per folder, however often the folder is listed.
skipped_junk=0
declare -A junk_counted
files_in() {
    local f
    FILES=()
    for f in "$1"/* "$1"/.[!.]*; do
        [[ -f $f ]] || continue
        if is_junk "$f"; then
            [[ -n ${junk_counted[$1]:-} ]] || skipped_junk=$((skipped_junk + 1))
            continue
        fi
        FILES+=("$f")
    done
    junk_counted[$1]=1
}

folders_0108=()
folders_09_10=()
for d in "$FINAL"/[01][0-9]*/; do
    d=${d%/}
    case ${d##*/} in
        0[1-8]*) folders_0108+=("${d##*/}") ;;
        09* | 10*) folders_09_10+=("${d##*/}") ;;
    esac
done

# --- Verification (before any copy) ----------------------------------------

echo "== Verifying snapshots"
mismatches=()

n_s22=0
n_s22_same=0
for folder in "${folders_0108[@]}"; do
    [[ -d $S22/$folder ]] || { mismatches+=("S22 has no folder $folder"); continue; }
    files_in "$S22/$folder"
    for f in "${FILES[@]}"; do
        name=${f##*/}
        [[ $name == [0-9]*.md ]] || continue
        n_s22=$((n_s22 + 1))
        if cmp -s "$f" "$BACKUP/$folder/$name"; then
            n_s22_same=$((n_s22_same + 1))
        else
            mismatches+=("S22 != BACKUP: $folder/$name")
        fi
    done
    # Every text in FINAL must also be in S22, so that none is dropped.
    files_in "$FINAL/$folder"
    for f in "${FILES[@]}"; do
        name=${f##*/}
        [[ $name == [0-9]*.md ]] || continue
        [[ -f $S22/$folder/$name ]] || mismatches+=("in FINAL but not in S22: $folder/$name")
    done
done
echo "S22 vs BACKUP (01–08 texts): $n_s22_same/$n_s22 identical"

n_fin=0
n_fin_same=0
for folder in "${folders_0108[@]}" "${folders_09_10[@]}"; do
    case $folder in 07c_* | 08_* | 09* | 10*) ;; *) continue ;; esac
    files_in "$FINAL/$folder"
    for f in "${FILES[@]}"; do
        name=${f##*/}
        n_fin=$((n_fin + 1))
        if cmp -s "$f" "$BACKUP/$folder/$name"; then
            n_fin_same=$((n_fin_same + 1))
        else
            mismatches+=("FINAL != BACKUP: $folder/$name")
        fi
    done
done
echo "FINAL vs BACKUP (07c, 08, 09a–09e, 10): $n_fin_same/$n_fin identical"

if ((${#mismatches[@]})); then
    echo "Verification failed:" >&2
    printf '  %s\n' "${mismatches[@]}" >&2
    exit 1
fi

# --- Copy plan --------------------------------------------------------------
# Each entry: snapshot <TAB> source <TAB> destination (relative) <TAB> FINAL copy
# (empty when FINAL has no counterpart).

plan=()
skipped_rule=()
add() { plan+=("$1"$'\t'"$2"$'\t'"$3"$'\t'"${4:-}"); }

for folder in "${folders_0108[@]}"; do
    files_in "$S22/$folder"
    for f in "${FILES[@]}"; do
        name=${f##*/}
        [[ $name == [0-9]*.md ]] && add S22 "$f" "texts/$folder/$name" "$FINAL/$folder/$name"
    done
    add BACKUP "$BACKUP/$folder/CHANGELOG.md" "texts/$folder/CHANGELOG.md" "$FINAL/$folder/CHANGELOG.md"
done

for folder in "${folders_09_10[@]}"; do
    files_in "$FINAL/$folder"
    for f in "${FILES[@]}"; do
        name=${f##*/}
        case $name in
            00_original_*) add FINAL "$f" "sources/originals/$folder/$name" "$f" ;;
            [0-9]*.md | CHANGELOG.md) add FINAL "$f" "texts/$folder/$name" "$f" ;;
            *) skipped_rule+=("FINAL/$folder/$name (unexpected file)") ;;
        esac
    done
done

refs=$BACKUP/_tools/refs
files_in "$refs"
for f in "${FILES[@]}"; do
    name=${f##*/}
    case $name in
        reference-pali-supplement.md) add BACKUP "$f" "sources/$name" ;;
        dn22_*.json) add BACKUP "$f" "sources/suttacentral/$name" ;;
        Bhikkhu-Manual-Reference.md) skipped_rule+=("BACKUP/_tools/refs/$name (replaced by upstream BM Markdown)") ;;
        ChantingGuide_Thanissaro.md) skipped_rule+=("BACKUP/_tools/refs/$name (not committed; location recorded)") ;;
        *) skipped_rule+=("BACKUP/_tools/refs/$name (unexpected file)") ;;
    esac
done

add BACKUP "$BACKUP/_tools/style.css" "templates/epub.css"
for font in Crimson Noto_Sans; do
    files_in "$EXERCISES/fonts/$font"
    for f in "${FILES[@]}"; do
        add EXERCISES "$f" "fonts/$font/${f##*/}"
    done
done
add SYSTEM "$NOTO_MATH" "fonts/Noto_Sans_Math/NotoSansMath-Regular.ttf"
add EXERCISES "$EXERCISES/exercises/style.typ" "templates/typst/style.typ"
add EXERCISES "$EXERCISES/scripts/simsapa_fmt.py" "scripts/simsapa_fmt.py"

for entry in "${plan[@]}"; do
    IFS=$'\t' read -r _ src _ _ <<<"$entry"
    [[ -f $src ]] || die "missing source file: $src"
done

# --- Overwrite check (before any copy) -------------------------------------

conflicts=()
for entry in "${plan[@]}"; do
    IFS=$'\t' read -r _ src rel _ <<<"$entry"
    if [[ -e $DEST/$rel ]] && ! cmp -s "$src" "$DEST/$rel"; then
        conflicts+=("$rel")
    fi
done

if ((${#conflicts[@]})) && [[ $FORCE == 0 ]]; then
    echo "These destination files differ from their source and would be overwritten:" >&2
    printf '  %s\n' "${conflicts[@]}" >&2
    echo "Nothing was copied. Re-run with --force to overwrite them." >&2
    exit 1
fi

# --- Copy and manifest ------------------------------------------------------

[[ $DRY_RUN == 1 ]] && echo "== Dry run: nothing is written"

declare -A per_folder_copied per_folder_same
manifest_rows=()
differs=()
n_copied=0
n_same=0

for entry in "${plan[@]}"; do
    IFS=$'\t' read -r snapshot src rel final <<<"$entry"
    dest=$DEST/$rel
    folder=${rel%/*}

    if [[ -e $dest ]] && cmp -s "$src" "$dest"; then
        n_same=$((n_same + 1))
        per_folder_same[$folder]=$((${per_folder_same[$folder]:-0} + 1))
    else
        if [[ $DRY_RUN == 0 ]]; then
            mkdir -p "${dest%/*}"
            cp -p "$src" "$dest"
        fi
        n_copied=$((n_copied + 1))
        per_folder_copied[$folder]=$((${per_folder_copied[$folder]:-0} + 1))
    fi

    sha=$(sha256sum "$src")
    sha=${sha%% *}
    if [[ -z $final ]]; then
        flag=n/a
        changed=n/a
    elif cmp -s "$final" "$src"; then
        flag=no
        changed=0
    else
        flag=yes
        changed=$(diff "$final" "$src" | grep -c '^>' || true)
        differs+=("$rel ($changed)")
    fi
    case $snapshot in
        S22) source=${src#"$S22"/} ;;
        FINAL) source=${src#"$FINAL"/} ;;
        BACKUP) source=${src#"$BACKUP"/} ;;
        EXERCISES) source=${src#"$EXERCISES"/} ;;
        *) source=$src ;;
    esac
    manifest_rows+=("$rel"$'\t'"$snapshot"$'\t'"$source"$'\t'"$sha"$'\t'"$flag"$'\t'"$changed")
done

# Source paths are relative to their snapshot's root (see
# docs/legacy-migration.md); SYSTEM paths are absolute.
manifest=$DEST/sources/MIGRATION-MANIFEST.tsv
manifest_text=$(
    printf 'dest\tsnapshot\tsource\tsha256\tdiffers_from_final\tchanged_lines_vs_final\n'
    printf '%s\n' "${manifest_rows[@]}" | LC_ALL=C sort
)
if [[ $DRY_RUN == 0 ]]; then
    if [[ -f $manifest ]] && [[ $(cat "$manifest") == "$manifest_text" ]]; then
        manifest_state="unchanged"
    else
        mkdir -p "${manifest%/*}"
        printf '%s\n' "$manifest_text" >"$manifest"
        manifest_state="written"
    fi
else
    manifest_state="not written (dry run)"
fi

# --- Summary ----------------------------------------------------------------

echo
echo "== Files per destination folder (copied / already identical)"
while IFS= read -r folder; do
    printf '  %-48s %3d / %3d\n' "$folder" "${per_folder_copied[$folder]:-0}" "${per_folder_same[$folder]:-0}"
done < <(printf '%s\n' "${!per_folder_copied[@]}" "${!per_folder_same[@]}" | LC_ALL=C sort -u)
echo "  total: $n_copied copied, $n_same already identical"
((${#conflicts[@]})) && echo "  overwritten (--force): ${#conflicts[@]}"

echo
echo "== Skipped"
echo "  macOS junk files: $skipped_junk"
for s in "${skipped_rule[@]}"; do
    echo "  $s"
done

echo
echo "== Files where FINAL differs from the chosen source (changed lines): ${#differs[@]}"
for d in "${differs[@]}"; do
    echo "  $d"
done

n_texts=0
n_changelogs=0
n_originals=0
for entry in "${plan[@]}"; do
    IFS=$'\t' read -r _ _ rel _ <<<"$entry"
    case $rel in
        texts/*/CHANGELOG.md) n_changelogs=$((n_changelogs + 1)) ;;
        texts/*/[0-9]*.md) n_texts=$((n_texts + 1)) ;;
        sources/originals/*) n_originals=$((n_originals + 1)) ;;
    esac
done

echo
echo "== Totals (actual / expected)"
echo "  texts:      $n_texts / $EXPECT_TEXTS"
echo "  changelogs: $n_changelogs / $EXPECT_CHANGELOGS"
echo "  originals:  $n_originals / $EXPECT_ORIGINALS"
echo "  manifest:   ${manifest#"$DEST"/} ($((${#manifest_rows[@]})) rows, $manifest_state)"

if ((n_texts != EXPECT_TEXTS || n_changelogs != EXPECT_CHANGELOGS || n_originals != EXPECT_ORIGINALS)); then
    echo "Totals do not match the expected counts." >&2
    exit 1
fi
