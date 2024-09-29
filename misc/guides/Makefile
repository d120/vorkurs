TOPTARGETS := all clean
OUT_DIR := pdfout/
FILES := $(wildcard *.tex)

# Compile LaTeX with jobname and environment variables
# $1: tex file to compile
# $2: jobname (output file name without extension)
# $3: environment variables
# $4: directory to compile in
define compile_latex_with_jobname_and_env
	cd $(4) && $(3) latexmk --shell-escape -synctex=1 -interaction=nonstopmode -file-line-error -lualatex -jobname=$(2) "$(1)"
endef

# Build LaTeX with jobname and environment variables, compile and copy to output directory
# $1: tex file to compile
# $2: jobname (output file name without extension)
# $3: environment variables
define build_latex_with_jobname_and_env
	$(eval DIR := $(dir $(1)))
	$(eval FILE := $(notdir $(1)))
	@echo -e "\e[1;32mCompiling \"$(FILE)\" in \"$(DIR)\" with jobname \"$(2)\"$<\e[0m"
	@$(call compile_latex_with_jobname_and_env,$(FILE),$(2),$(3),$(DIR))
	@echo -e "\e[1;32mSuccessfully compiled \"$(FILE)\" in \"$(DIR)\" with jobname \"$(2)\"$<\e[0m"
	@mkdir -p $(OUT_DIR)
	@cp $(DIR)/$(2).pdf $(OUT_DIR)/
endef

all:
	$(MAKE) clean
	$(MAKE) compile

$(FILES:.tex=.tex.regular):
	$(eval FILE := $(patsubst %.tex.regular,%.tex,$@))
	$(call build_latex_with_jobname_and_env,$(FILE),$(patsubst %.tex,%,$(notdir $(FILE))),)

$(FILES:.tex=.tex.darkmode):
	$(eval FILE := $(patsubst %.tex.darkmode,%.tex,$@))
	$(call build_latex_with_jobname_and_env,$(FILE),$(patsubst %.tex,%-dark,$(notdir $(FILE))),DARK_MODE=1)

$(FILES:.tex=.tex.highcontrast):
	$(eval FILE := $(patsubst %.tex.highcontrast,%.tex,$@))
	$(call build_latex_with_jobname_and_env,$(FILE),$(patsubst %.tex,%-high-contrast,$(notdir $(FILE))),DARK_MODE=2)

compile: $(FILES:.tex=.tex.regular) $(FILES:.tex=.tex.darkmode) $(FILES:.tex=.tex.highcontrast)
	@echo -e "\e[1;42mAll Done. PDFs can be found in $(OUT_DIR)\e[0m"

# Remove files with a specific pattern recursively
# $1: pattern to match
# $2: additional global find parameters
# $3: additional directories to exclude
# Example: $(call remove_files,**/*.pdf, -maxdepth 1)
# explanation of find parameters:
# -depth: process each directory's contents before the directory itself (otherwise, the directory itself would be deleted first leading to errors when processing the contents)
# -not \( -path "*/.git/*" -prune \): exclude .git directories
# -wholename '$(1)': match the pattern
# -exec rm -rf {} \;: remove the matched files (-r also works on files, but is needed for directories)
define remove_files
	@find . $(if $(strip $(2)),$(2),) -depth -not \( -path "*/.git/*" $(foreach dir,$(strip $(3)),-o -path "*/$(dir)*") -prune \) -wholename '$(1)' -exec rm -rf {} \;
endef

clean:
	@echo -e "\e[1;34mCleaning up leftover build files...$<\e[0m"
	@latexmk -C -f
	$(call remove_files,**/options.cfg)
	$(call remove_files,**/*.pdf,,$(OUT_DIR) media)
	$(call remove_files,**/*.aux)
	$(call remove_files,**/*.fdb_latexmk)
	$(call remove_files,**/*.fls)
	$(call remove_files,**/*.len)
	$(call remove_files,**/*.listing)
	$(call remove_files,**/*.log)
	$(call remove_files,**/*.out)
	$(call remove_files,**/*.synctex.gz)
	$(call remove_files,**/*.toc)
	$(call remove_files,**/*.nav)
	$(call remove_files,**/*.snm)
	$(call remove_files,**/*.vrb)
	$(call remove_files,**/*.bbl)
	$(call remove_files,**/*.bbl-SAVE-ERROR)
	$(call remove_files,**/*.bcf-SAVE-ERROR)
	$(call remove_files,**/*.blg)
	$(call remove_files,**/*.idx)
	$(call remove_files,**/*.ilg)
	$(call remove_files,**/*.ind)
	$(call remove_files,**/*.pyg)
	$(call remove_files,**/*.bcf)
	$(call remove_files,**/*.xmpdata)
	$(call remove_files,**/*.xmpi)
	$(call remove_files,**/*.run.xml)
	$(call remove_files,**/*.bak[0-9]*)
	$(call remove_files,**/_minted-*)
	@echo -e "\e[1;44mDone cleaning up leftover build files.$<\e[0m"

cleanBuild:
	@echo -e "\e[1;34mCleaning up build directory...$<\e[0m"
	@rm -rf $(OUT_DIR)
	@echo -e "\e[1;44mDone cleaning up build directory.$<\e[0m"

cleanAll: clean cleanBuild
