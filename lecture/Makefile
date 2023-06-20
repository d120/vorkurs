TOPTARGETS := all clean
OUT_DIR := pdfout/

define compile_latex_with_jobname_and_env
	cd $(4) && $(3) latexmk --shell-escape -synctex=1 -interaction=nonstopmode -file-line-error -lualatex -jobname=$(2) "$(1)"
endef

define build_latex_with_jobname_and_env
	$(eval DIR := $(dir $(1)))
	$(eval FILE := $(notdir $(1)))
	@echo -e "\e[1;32mCompiling \"$(FILE)\" in \"$(DIR)\" with jobname \"$(2)\"$<\e[0m"
	@$(call compile_latex_with_jobname_and_env,$(FILE),$(2),$(3),$(DIR))
	@echo -e "\e[1;32mSuccessfully compiled \"$(FILE)\" in \"$(DIR)\" with jobname \"$(2)\"$<\e[0m"
	@mkdir -p $(OUT_DIR)
	@mv $(DIR)/$(2).pdf $(OUT_DIR)/
endef

SUBDIRS := $(wildcard */*.tex)

all:
	$(MAKE) clean
	$(MAKE) compile

compile: $(SUBDIRS:.tex=.tex.regular) $(SUBDIRS:.tex=.tex.darkmode) $(SUBDIRS:.tex=.tex.highcontrast)
	@echo -e "\e[1;42mAll Done. PDFs can be found in $(OUT_DIR)\e[0m"

$(SUBDIRS:.tex=.tex.regular):
	$(eval FILE := $(patsubst %.tex.regular,%.tex,$@))
	$(call build_latex_with_jobname_and_env,$(FILE),$(patsubst %.tex,%,$(notdir $(FILE))),)

$(SUBDIRS:.tex=.tex.darkmode):
	$(eval FILE := $(patsubst %.tex.darkmode,%.tex,$@))
	$(call build_latex_with_jobname_and_env,$(FILE),$(patsubst %.tex,%-dark,$(notdir $(FILE))),DARK_MODE=1)

$(SUBDIRS:.tex=.tex.highcontrast):
	$(eval FILE := $(patsubst %.tex.highcontrast,%.tex,$@))
	$(call build_latex_with_jobname_and_env,$(FILE),$(patsubst %.tex,%-high-contrast,$(notdir $(FILE))),DARK_MODE=2)

# recursive slides helper
define recurse_cp
	$(eval DIR := $(dir $(1)))
	$(eval RECFILE := $(notdir $(1)))
	@echo -e "\e[1;32mCompiling Recursive slides \"$(RECFILE)\" in \"$(DIR)\" with jobname \"$(2)\". Iteration $(4)/5\e[0m"
	@$(call compile_latex_with_jobname_and_env,$(RECFILE),$(2),$(3),$(DIR))
	@mv $(DIR)/$(2).pdf $(DIR)/$(2)_tmp.pdf
endef

define recursive_cp_helper
	$(call recurse_cp,$(1),$(2),$(3),1)
	$(call recurse_cp,$(1),$(2),$(3),2)
	$(call recurse_cp,$(1),$(2),$(3),3)
	$(call recurse_cp,$(1),$(2),$(3),4)
	$(call recurse_cp,$(1),$(2),$(3),5)
	@echo -e "\e[1;32mPreparation for recursive slides \"$(1)\" in \"$(2)\" with jobname \"$(2)\" complete. Now compiling normally$<\e[0m"
	$(call build_latex_with_jobname_and_env,$(1),$(2),$(3))
endef

# more specific rule for recursive slides that overwrites generic above
06_Funktionen/06_Funktionen.tex.regular:
	$(eval FILE := $(patsubst %.tex.regular,%.tex,$@))
	$(call recursive_cp_helper,$(FILE),$(patsubst %.tex,%,$(notdir $(FILE))),)

06_Funktionen/06_Funktionen.tex.darkmode:
	$(eval FILE := $(patsubst %.tex.darkmode,%.tex,$@))
	$(call recursive_cp_helper,$(FILE),$(patsubst %.tex,%-dark,$(notdir $(FILE))),DARK_MODE=1)

06_Funktionen/06_Funktionen.tex.highcontrast:
	$(eval FILE := $(patsubst %.tex.highcontrast,%.tex,$@))
	$(call recursive_cp_helper,$(FILE),$(patsubst %.tex,%-high-contrast,$(notdir $(FILE))),DARK_MODE=2)

clean:
	@echo -e "\e[1;31mCleaning ignored files$<\e[0m"
	@latexmk -C -f
	@find . -wholename '**/options.cfg' -delete
	@find . -wholename '**/*.pdf' -delete
	@find . -wholename '**/*.aux' -delete
	@find . -wholename '**/*.fdb_latexmk' -delete
	@find . -wholename '**/*.fls' -delete
	@find . -wholename '**/*.len' -delete
	@find . -wholename '**/*.listing' -delete
	@find . -wholename '**/*.log' -delete
	@find . -wholename '**/*.out' -delete
	@find . -wholename '**/*.synctex.gz' -delete
	@find . -wholename '**/*.toc' -delete
	@find . -wholename '**/*.nav' -delete
	@find . -wholename '**/*.snm' -delete
	@find . -wholename '**/*.vrb' -delete
	@find . -wholename '**/*.bbl' -delete
	@find . -wholename '**/*.blg' -delete
	@find . -wholename '**/*.idx' -delete
	@find . -wholename '**/*.ilg' -delete
	@find . -wholename '**/*.ind' -delete
	@find . -wholename '**/*.pyg' -delete
	@find . -wholename '**/*.bak[0-9]*' -delete
	@find . -wholename '**/_minted-*' -delete

cleanBuild:
	@echo "Cleaning our dir..."
	@rm -rf $(OUT_DIR)

cleanAll: clean cleanBuild

.PHONY: $(TOPTARGETS) $(SUBDIRS)
