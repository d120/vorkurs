
OUT_DIR := pdfout/
# find all makefiles in subdirectories
FILES := $(shell find . -mindepth 2 -name 'Makefile' -not -path './.git/*' -not -path './.devcontainer')

$(FILES:Makefile=Makefile.all):
	$(eval FILE := $(patsubst %.all,%,$@))
	@$(MAKE) -C $(dir $(FILE)) -f $(notdir $(FILE)) all

$(FILES:Makefile=Makefile.compile):
	$(eval FILE := $(patsubst %.compile,%,$@))
	@$(MAKE) -C $(dir $(FILE)) -f $(notdir $(FILE)) compile

$(FILES:Makefile=Makefile.clean):
	$(eval FILE := $(patsubst %.clean,%,$@))
	@$(MAKE) -C $(dir $(FILE)) -f $(notdir $(FILE)) clean

$(FILES:Makefile=Makefile.cleanBuild):
	$(eval FILE := $(patsubst %.cleanBuild,%,$@))
	@$(MAKE) -C $(dir $(FILE)) -f $(notdir $(FILE)) cleanBuild

$(FILES:Makefile=Makefile.cleanAll):
	$(eval FILE := $(patsubst %.cleanAll,%,$@))
	@$(MAKE) -C $(dir $(FILE)) -f $(notdir $(FILE)) cleanAll

all: $(FILES:Makefile=Makefile.all)
	@echo -e "\e[1;42mAll Done. PDFs can be found in $(OUT_DIR)\e[0m"

compile: $(FILES:Makefile=Makefile.compile)
	@echo -e "\e[1;42mAll Done. PDFs can be found in $(OUT_DIR)\e[0m"

clean: $(FILES:Makefile=Makefile.clean)
	@echo -e "\e[1;44mCleaned up all subdirectories.\e[0m"

cleanBuild: $(FILES:Makefile=Makefile.cleanBuild)
	@echo -e "\e[1;44mCleaned up build dir in all subdirectories.\e[0m"

cleanAll: $(FILES:Makefile=Makefile.cleanAll)
	@echo -e "\e[1;44mCleaned up all subdirectories + build dirs.\e[0m"
