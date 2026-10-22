# Build and check targets. See README.md for usage.

PYTHON ?= python3
PANDOC ?= pandoc
EPUBCHECK ?= epubcheck

BOOKS := $(notdir $(wildcard books/*))
TEXTS := $(wildcard texts/*/[0-9]*.md)
# Everything the assembled Markdown depends on besides the book's own files.
BUILD_SCRIPTS := $(wildcard scripts/*.py scripts/chantlib/*.py) docs/style-spec.md
# Fonts embedded in each EPUB; templates/epub.css has their @font-face rules.
EPUB_FONTS := $(addprefix fonts/Crimson/Crimson-,Roman.otf Italic.otf Bold.otf BoldItalic.otf) \
	fonts/Noto_Sans/NotoSans-Regular.ttf \
	fonts/Noto_Sans_Math/NotoSansMath-Regular.ttf

.PHONY: help check-tools test clean all epub pdf book covers \
	lint lint-fix compare index dpd-check fetch-sources epubcheck

help:
	@echo "Targets:"
	@echo "  check-tools    check required tools and the Simsapa API"
	@echo "  test           run the unit tests"
	@echo "  all            epub + pdf for all books"
	@echo "  epub / pdf     all books in one format"
	@echo "  book BOOK=id   one book, both formats"
	@echo "  covers         render all covers"
	@echo "  epubcheck      validate all built EPUBs with epubcheck"
	@echo "  lint           lint all texts (lint-fix applies safe fixes)"
	@echo "  compare        check Pāli lines against sources/"
	@echo "  index          cross-file consistency report"
	@echo "  dpd-check      check word tables against DPD via Simsapa"
	@echo "  fetch-sources  clone/update sources/upstream/ at pinned commits"
	@echo "  clean          remove build/"

check-tools:
	@scripts/check-tools.sh

test:
	$(PYTHON) -m unittest discover -s tests
	tests/test_migrate.sh

fetch-sources:
	@scripts/fetch-sources.sh

lint:
	@$(PYTHON) scripts/lint.py $(TEXTS)

lint-fix:
	@$(PYTHON) scripts/lint.py --fix $(TEXTS)

clean:
	rm -rf build

# ---------------------------------------------------------------- books
# docs/book-build.md describes the pipeline: books/<book>/metadata.txt and
# the book's texts → scripts/assemble.py → build/tmp/<book>.md → pandoc.

all: epub pdf

epub: $(BOOKS:%=build/epub/%.epub)

book:
	@test -n "$(BOOK)" -a -f "books/$(BOOK)/metadata.txt" || \
		{ echo "usage: make book BOOK=<id>, one of: $(BOOKS)" >&2; exit 2; }
	@$(MAKE) --no-print-directory build/epub/$(BOOK).epub

epubcheck:
	@ls build/epub/*.epub >/dev/null 2>&1 || { echo "no EPUBs in build/epub/; run make epub" >&2; exit 1; }
	@fail=0; for f in build/epub/*.epub; do \
		echo "epubcheck $$f"; $(EPUBCHECK) "$$f" || fail=1; \
	done; exit $$fail

.SECONDEXPANSION:
.PRECIOUS: build/tmp/%.md

# Each book's text files come from its metadata, through build/deps/<book>.mk
# (written by assemble.py --deps). The deps file is replaced only when the
# file list changes, so the books are not rebuilt for nothing.
ifneq ($(filter all epub pdf book covers build/%,$(MAKECMDGOALS)),)
-include $(BOOKS:%=build/deps/%.mk)
endif

build/deps/%.mk:
	@mkdir -p $(@D)
	@$(PYTHON) scripts/assemble.py --deps $* > $@.tmp && { cmp -s $@.tmp $@ || mv $@.tmp $@; }; rm -f $@.tmp

build/tmp/%.md: $$(wildcard books/$$*/*) $(BUILD_SCRIPTS) $$(wildcard build/covers/$$*.png)
	$(PYTHON) scripts/assemble.py $*

# A fatal or error from epubcheck removes the EPUB, so make does not take
# it as up to date (docs/book-build.md).
build/epub/%.epub: build/tmp/%.md templates/epub.css $(EPUB_FONTS)
	@mkdir -p $(@D)
	$(PANDOC) --defaults build/tmp/$*.pandoc.yaml --css templates/epub.css \
		$(EPUB_FONTS:%=--epub-embed-font=%) -o $@
	@$(EPUBCHECK) $@ || { rm -f $@; echo "epubcheck failed; removed $@" >&2; exit 1; }

pdf covers compare index dpd-check:
	@echo "make $@: not implemented yet"
