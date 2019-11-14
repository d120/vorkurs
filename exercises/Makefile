IN = Aufgaben.tex
SHIPDIR = _build
POST = $(shell /bin/bash -c 'if which pplatex > /dev/null; then echo "| pplatex -i -"; else echo "> /dev/null"; fi')
PDFLATEX = pdflatex -interaction=nonstopmode

all:	 $(shell /bin/bash -c 'echo Aufgabe_{1,2,3,4}_{sol,nosol}.pdf') ship clean

Aufgabe_%: Aufgabe_%_sol.pdf Aufgabe_%_nosol.pdf

Aufgabe_%_nosol.pdf: Aufgaben_nosol.tex
	$(PDFLATEX) -jobname="Übung_$*" -shell-escape "\newcounter{ex} \setcounter{ex}{$*} \input{Aufgaben_nosol.tex}" $(POST)

Aufgabe_%_sol.pdf: Aufgaben_sol.tex
	$(PDFLATEX) -jobname="Lösung_$*" -shell-escape "\newcounter{ex} \setcounter{ex}{$*} \input{Aufgaben_sol.tex}" $(POST)

Aufgaben_nosol.tex: Aufgaben.tex
	sed -r s/'\\setboolean\{sln\}\{(true|false)\}'/"\\\\setboolean{sln}{false}"/ $(IN) > Aufgaben_nosol.tex

Aufgaben_sol.tex: Aufgaben.tex
	sed -r s/'\\setboolean\{sln\}\{(true|false)\}'/"\\\\setboolean{sln}{true}"/ $(IN) > Aufgaben_sol.tex

ship:
	mkdir -p $(SHIPDIR)
	mv *.pdf $(SHIPDIR)

clean:
	rm -f *.aux *.log *.out Aufgaben_*sol.tex *.pdf
	rm -rf _minted*
