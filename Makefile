# Build and check targets. See README.md for usage.

PYTHON ?= python3

BOOKS := $(notdir $(wildcard books/*))

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

clean:
	rm -rf build

all epub pdf book covers lint lint-fix compare index dpd-check epubcheck:
	@echo "make $@: not implemented yet"
