
OUT_DIR := _build/

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

FILES := $(wildcard Aufgabe*.tex)

all:
	$(MAKE) clean
	$(MAKE) compile

$(FILES:.tex=.tex.regular):
	$(eval FILE := $(patsubst %.tex.regular,%.tex,$@))
	$(call build_latex_with_jobname_and_env,$(FILE),$(patsubst %.tex,%,$(FILE)),)

$(FILES:.tex=.tex.sol.regular):
	$(eval FILE := $(patsubst %.tex.sol.regular,%.tex,$@))
	$(call build_latex_with_jobname_and_env,$(FILE),$(patsubst %.tex,%-sol,$(FILE)),SOLUTION=1)

$(FILES:.tex=.tex.darkmode):
	$(eval FILE := $(patsubst %.tex.darkmode,%.tex,$@))
	$(call build_latex_with_jobname_and_env,$(FILE),$(patsubst %.tex,%-darkmode,$(FILE)),DARK_MODE=1)

$(FILES:.tex=.tex.sol.darkmode):
	$(eval FILE := $(patsubst %.tex.sol.darkmode,%.tex,$@))
	$(call build_latex_with_jobname_and_env,$(FILE),$(patsubst %.tex,%-sol-darkmode,$(FILE)),DARK_MODE=1 SOLUTION=1)

compile: $(FILES:.tex=.tex.regular) $(FILES:.tex=.tex.sol.regular) $(FILES:.tex=.tex.darkmode) $(FILES:.tex=.tex.sol.darkmode)
	@echo -e "\e[1;42mAll Done. PDFs can be found in $(OUT_DIR)\e[0m"

clean:
	@echo -e "\e[1;31mCleaning up leftover build files...$<\e[0m"
	@latexmk -C -f
	@rm -f options.cfg
	@rm -f *.pdf
	@rm -f *.aux
	@rm -f *.fdb_latexmk
	@rm -f *.fls
	@rm -f *.len
	@rm -f *.listing
	@rm -f *.log
	@rm -f *.out
	@rm -f *.synctex.gz
	@rm -f *.toc
	@rm -f *.nav
	@rm -f *.snm
	@rm -f *.vrb
	@rm -f *.bbl
	@rm -f *.blg
	@rm -f *.bak[0-9]*
	@rm -rf _minted-*

cleanBuild:
	@echo "\e[1;31mCleaning build dir...$<\e[0m"
	@rm -rf $(OUT_DIR)

cleanAll: clean cleanBuild
