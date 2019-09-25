TOPTARGETS := all clean
PDFLATEX_FLAGS := -shell-escape #-interaction=batchmode
PDFLATEX := pdflatex $(PDFLATEX_FLAGS)
COMPILE_PRINT := \e[1;32mCompiling$<\e[0m
OUT_DIR := pdfout/

DOCS := $(wildcard *.tex)

all: $(DOCS)
	@echo -e "\e[1;42mPDFs can be found in $(OUT_DIR)\e[0m"

$(DOCS):
	$(eval FILE := $(notdir $@))
	@echo -e "$(COMPILE_PRINT) $(FILE)"
	@$(PDFLATEX) $(FILE) && $(PDFLATEX) $(FILE) && $(PDFLATEX) $(FILE)
clean:
	@echo -e "\e[1;31mCleaning ignored files$<\e[0m"
	@git clean -f -d -X 			# remove all ignored files

.PHONY: $(TOPTARGETS) $(DOCS)
