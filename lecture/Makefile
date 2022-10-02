TOPTARGETS := all clean
PDFLATEX_FLAGS := -shell-escape
PDFLATEX_PREAMBLE :=
PDFLATEX := pdflatex $(PDFLATEX_FLAGS)
COMPILE_PRINT := \e[1;32mCompiling$<\e[0m
OUT_DIR := pdfout/

ifeq ($(VORKURS_NOTES), 1)
	PDFLATEX_PREAMBLE := \setbeameroption{show notes on second screen}
endif

define pdflatex_cmd
	$(PDFLATEX) $(PDFLATEX_FLAGS) '\AtBeginDocument{$(PDFLATEX_PREAMBLE)}\input{$(1)}'
endef

SUBDIRS := $(wildcard */*.tex)

all: $(SUBDIRS)
	@echo -e "\e[1;42mPDFs can be found in $(OUT_DIR)\e[0m"

$(SUBDIRS):
	$(eval DIR := $(dir $@))
	$(eval FILE := $(notdir $@))
	@echo -e "$(COMPILE_PRINT) $(FILE)"
	@cd $(DIR) && $(call pdflatex_cmd, $(FILE)) && $(call pdflatex_cmd, $(FILE)) && $(call pdflatex_cmd, $(FILE))
	@# copy PDF file to outdir
	@mkdir -p $(OUT_DIR)
	@cp $(basename $@).pdf $(OUT_DIR)/
	@echo

# recursive slides helper
define recurse_cp
	@cd $(DIR) && $(call pdflatex_cmd, $(FILE)) && $(call pdflatex_cmd, $(FILE)) && $(call pdflatex_cmd, $(FILE))
	@cp $(basename $@).pdf $(basename $@)_tmp.pdf
endef

# more specific rule for recursive slides that overwrites generic above
06_Funktionen/06_05_Rekursion.tex:
	$(eval DIR := $(dir $@))
	$(eval FILE := $(notdir $@))
	@echo -e "$(COMPILE_PRINT) $(FILE)"
	@# original without recurse
	$(call recurse_cp)
	@# recurse, use preamble for variable definition that controls recursive include
	$(eval PDFLATEX_PREAMBLE_OLD := $(PDFLATEX_PREAMBLE))
	$(eval PDFLATEX_PREAMBLE := $(PDFLATEX_PREAMBLE_OLD) \def \vorkursRecurse{})
	@# recursive
	$(call recurse_cp)
	$(call recurse_cp)
	$(call recurse_cp)
	$(call recurse_cp)
	$(call recurse_cp)
	$(call recurse_cp)
	$(call recurse_cp)
	@# restore environment
	$(eval PDFLATEX_PREAMBLE := $(PDFLATEX_PREAMBLE_OLD))
	@# copy PDF file to outdir
	@mkdir -p $(OUT_DIR)
	@cp $(basename $@).pdf $(OUT_DIR)/
	@echo

clean:
	@echo -e "\e[1;31mCleaning ignored files$<\e[0m"
	@git clean -f -d -X 			# remove all ignored files

.PHONY: $(TOPTARGETS) $(SUBDIRS)
