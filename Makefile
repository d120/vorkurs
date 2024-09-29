.DEFAULT_GOAL := all

OUT_DIR := pdfout/
# find all makefiles in subdirectories
MAKEFILES := $(shell find . -mindepth 2 -name 'Makefile' -not -path './.git/**/*' -not -path './.devcontainer/**/*')

$(MAKEFILES:Makefile=Makefile.all):
	$(eval MAKEFILE := $(patsubst %.all,%,$@))
	@$(MAKE) -C $(dir $(MAKEFILE)) -f $(notdir $(MAKEFILE)) all
	@mkdir -p $(OUT_DIR)
	@cp $(dir $(MAKEFILE))/$(OUT_DIR)/*.pdf $(OUT_DIR)

$(MAKEFILES:Makefile=Makefile.compile):
	$(eval MAKEFILE := $(patsubst %.compile,%,$@))
	$(MAKE) -C $(dir $(MAKEFILE)) -f $(notdir $(MAKEFILE)) compile
	@mkdir -p $(OUT_DIR)
	@cp $(dir $(MAKEFILE))/$(OUT_DIR)/*.pdf $(OUT_DIR)

$(MAKEFILES:Makefile=Makefile.clean):
	$(eval MAKEFILE := $(patsubst %.clean,%,$@))
	$(MAKE) -C $(dir $(MAKEFILE)) -f $(notdir $(MAKEFILE)) clean

# $(MAKEFILES:Makefile=Makefile.cleanBuild):
# 	$(eval MAKEFILE := $(patsubst %.cleanBuild,%,$@))
# 	@$(MAKE) -C $(dir $(MAKEFILE)) -f $(notdir $(MAKEFILE)) cleanBuild

$(MAKEFILES:Makefile=Makefile.cleanAll):
	$(eval MAKEFILE := $(patsubst %.cleanAll,%,$@))
	@$(MAKE) -C $(dir $(MAKEFILE)) -f $(notdir $(MAKEFILE)) cleanAll

all: $(MAKEFILES:Makefile=Makefile.all)
	@echo -e "\e[1;42mAll Done. PDFs can be found in $(OUT_DIR)\e[0m"

compile: $(MAKEFILES:Makefile=Makefile.compile)
	@echo -e "\e[1;42mAll Done. PDFs can be found in $(OUT_DIR)\e[0m"

clean: $(MAKEFILES:Makefile=Makefile.clean)
	@echo -e "\e[1;44mCleaned up all subdirectories.\e[0m"

cleanBuild:
	@echo -e "\e[1;34mCleaning up build directory...$<\e[0m"
	@rm -rf $(OUT_DIR)
	@echo -e "\e[1;44mDone cleaning up build directory.$<\e[0m"

cleanAll: $(MAKEFILES:Makefile=Makefile.cleanAll) cleanBuild
	@echo -e "\e[1;44mCleaned up all subdirectories + build dirs.\e[0m"
