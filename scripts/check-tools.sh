#!/usr/bin/env bash
# Check that the tools needed to build and check the books are installed.
#
# Prints OK, TOO OLD or MISSING for each tool, with an install hint for this
# system. Exits non-zero only if a required tool is missing or too old.
# Optional tools and the Simsapa API are reported but never fail the check.

set -euo pipefail

# Minimum versions. Keep in sync with README.md and CLAUDE.md.
MIN_PANDOC=3.1.2   # first release with the typst writer
MIN_TYPST=0.13
MIN_PYTHON=3.11

failed=0

# version_ge A B: true if version A >= version B (dot-separated numbers).
version_ge() {
    local IFS=.
    local -a a=($1) b=($2)
    local i x y
    for ((i = 0; i < ${#a[@]} || i < ${#b[@]}; i++)); do
        x=${a[i]:-0}
        y=${b[i]:-0}
        ((10#$x > 10#$y)) && return 0
        ((10#$x < 10#$y)) && return 1
    done
    return 0
}

# First dotted version number found in a string.
extract_version() {
    grep -oE '[0-9]+(\.[0-9]+)+' <<<"$1" | head -n 1 || true
}

detect_os() {
    if [[ "$(uname -s)" == Darwin ]]; then
        echo macos
    elif [[ -r /etc/os-release ]]; then
        # shellcheck disable=SC1091
        . /etc/os-release
        case " ${ID:-} ${ID_LIKE:-} " in
            *" arch "*) echo arch ;;
            *" debian "* | *" ubuntu "*) echo debian ;;
            *) echo other ;;
        esac
    else
        echo other
    fi
}

OS=$(detect_os)

hint() {
    local tool=$1 arch=$2 macos=$3 debian=$4
    case $OS in
        arch) echo "    install: $arch" ;;
        macos) echo "    install: $macos" ;;
        debian) echo "    install: $debian" ;;
        *)
            echo "    install (Arch):          $arch"
            echo "    install (macOS):         $macos"
            echo "    install (Debian/Ubuntu): $debian"
            ;;
    esac
}

hint_for() {
    case $1 in
        pandoc) hint pandoc "sudo pacman -S pandoc-cli" "brew install pandoc" \
            "the .deb from https://github.com/jgm/pandoc/releases (Debian 12's pandoc 2.17 is too old)" ;;
        typst) hint typst "sudo pacman -S typst" "brew install typst" \
            "the binary from https://github.com/typst/typst/releases, or: cargo install --locked typst-cli" ;;
        python3) hint python3 "sudo pacman -S python" "brew install python" "sudo apt install python3" ;;
        make) hint make "sudo pacman -S make" "brew install make (or: xcode-select --install)" "sudo apt install make" ;;
        curl) hint curl "sudo pacman -S curl" "brew install curl" "sudo apt install curl" ;;
        git) hint git "sudo pacman -S git" "brew install git" "sudo apt install git" ;;
        jq) hint jq "sudo pacman -S jq" "brew install jq" "sudo apt install jq" ;;
        epubcheck) hint epubcheck "yay -S epubcheck (AUR; needs Java), or the jar from https://github.com/w3c/epubcheck/releases" \
            "brew install epubcheck" "sudo apt install epubcheck" ;;
    esac
}

# check TOOL REQUIRED(yes/no) MIN_VERSION(or empty) VERSION_COMMAND...
check() {
    local tool=$1 required=$2 min=$3
    shift 3
    local label
    [[ $required == yes ]] && label=required || label=optional

    if ! command -v "$tool" >/dev/null 2>&1; then
        printf '%-10s MISSING   (%s)\n' "$tool" "$label"
        hint_for "$tool"
        if [[ $required == yes ]]; then failed=1; fi
        return 0
    fi

    local out version
    out=$("$@" 2>&1 | head -n 1 || true)
    version=$(extract_version "$out")

    if [[ -n $min ]]; then
        if [[ -z $version ]]; then
            printf '%-10s TOO OLD   (could not read version; need >= %s)\n' "$tool" "$min"
            hint_for "$tool"
            if [[ $required == yes ]]; then failed=1; fi
        elif version_ge "$version" "$min"; then
            printf '%-10s OK        %s (>= %s)\n' "$tool" "$version" "$min"
        else
            printf '%-10s TOO OLD   %s (need >= %s)\n' "$tool" "$version" "$min"
            hint_for "$tool"
            if [[ $required == yes ]]; then failed=1; fi
        fi
    else
        printf '%-10s OK        %s\n' "$tool" "${version:-(version unknown)}"
    fi
}

echo "Required tools:"
check pandoc yes "$MIN_PANDOC" pandoc --version
check typst yes "$MIN_TYPST" typst --version
check python3 yes "$MIN_PYTHON" python3 --version
check make yes "" make --version
check curl yes "" curl --version
check git yes "" git --version
check epubcheck yes "" epubcheck --version

echo
echo "Optional tools:"
check jq no "" jq --version

echo
echo "Simsapa API (needed only for dpd-check, lookup, gloss and the SuttaCentral texts of compare):"
port=4848
if [[ -n ${SIMSAPA_DIR:-} && -r "$SIMSAPA_DIR/api-port.txt" ]]; then
    port=$(tr -d '[:space:]' <"$SIMSAPA_DIR/api-port.txt")
fi
if command -v curl >/dev/null 2>&1 &&
    health=$(curl -s --max-time 2 "http://localhost:$port/health") && [[ -n $health ]]; then
    app_version=$(grep -oE '"app_version" *: *"[^"]*"' <<<"$health" | sed -E 's/.*"([^"]*)"$/\1/' || true)
    dpd_version=$(grep -oE '"dpd_version" *: *"[^"]*"' <<<"$health" | sed -E 's/.*"([^"]*)"$/\1/' || true)
    printf '%-10s available on port %s%s%s\n' simsapa "$port" "${app_version:+ (app $app_version)}" "${dpd_version:+, DPD $dpd_version}"
    # The app version did not change when these fields were added, so probe
    # /lookup_forms for them: form_grammar_raw (DPD's parses of a form) and
    # construction_summary (null when dpd.sqlite3 predates the column).
    lookup=$(curl -s --max-time 5 -X POST "http://localhost:$port/lookup_forms" \
        -H 'Content-Type: application/json' -d '{"forms":["dhammo"]}' || true)
    if ! grep -q '"results"' <<<"$lookup"; then
        echo "    no /lookup_forms route: simsapa.py needs a newer Simsapa (1.1.0-alpha.2 or later)"
    elif ! grep -q '"form_grammar_raw"' <<<"$lookup"; then
        echo "    /lookup_forms has no form_grammar_raw: update Simsapa for simsapa.py check and gloss"
    elif grep -q '"construction_summary" *: *null' <<<"$lookup"; then
        echo "    construction_summary is null: the installed dpd.sqlite3 predates it; update the DPD database"
    fi
else
    printf '%-10s not running on port %s\n' simsapa "$port"
    echo "    start the Simsapa app and enable its localhost API; see docs/simsapa-localhost-api-search-endpoints.md"
fi

echo
if ((failed)); then
    echo "Some required tools are missing or too old."
    exit 1
fi
echo "All required tools are present."
