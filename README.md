# Programmiervorkurs

Dieses Projekt enthält sämtliches Material des Programmiervorkurses der Fachschaft Informatik, TU Darmstadt. Der Programmiervorkurs findet alljährlich zu Beginn des Wintersemesters statt. Mehr Informationen zum Ablauf des Kurses finden sich auf [unserer Webseite](https://d120.de/vorkurs).  
Dieses Repository enthält hauptsächlich die Quellen des Vorkursmaterials, die erstellten Unterlagen finden sich im jeweiligen Moodle-Kurs, teilweise auch als Release.

## Inhalte und Struktur

Das Repository ist besteht aus folgenden Inhalten in eigenen Verzeichnissen:

* `codingchallenges`: Aufgabenstellungen und Referenzimplementierungen der Coding-Challenges sortiert nach Jahr
* `lecture`: Vorlesungsfolien
* `livecoding`: Hinweise für das Live-Coding
* `exercises`: Übungen und Lösungsvorschläge
* `misc`: Weitere Dokumente und Skripte
* `shared`: Allgemeine, gemeinsam verwendete LaTeX-Definitionen

## Erzeugen des Materials
Die Vorlesungsfolien, Übungen, Coding-Challenges und einige andere Dokumente stehen als LaTeX-Quelltext bereit. Sie setzen voraus:
- installierte LaTeX-Distribution (z.B. MikTex oder TeXLive)
- eine funktionierende Installation das TU Darmstadt [Corporate Designs](https://ctan.org/pkg/tuda-ci?lang=de) voraus (inklusive Logo!)
- Installation der [AlgoTeX-Vorlage](https://github.com/TUDalgo/AlgoTeX#algotex---die-latex-vorlage-der-fop-und-aud)
- Das python-Paket `minted` (z.B. über `pip install minted`) für Syntax-Highlighting

Zur einfachen Erstellung der Inhalte stehen UNIX Makefiles bereit, Details dazu sind den jeweiligen Verzeichnis zu entnehmen. Um alle PDFs zu erzeugen, kann im Hauptverzeichnis einfach `make -j` ausgeführt werden (-j nutzt alle verfügbaren Prozessorkerne und kompilliert so schneller). Die erzeugten PDFs liegen dann im Ordner `pdfout`.

## Dev Setup
### Automatisches Setup mit Devcontainer (empfohlen)
- [Docker](https://www.docker.com/) installieren
- [VS-Code](https://code.visualstudio.com/) (oder die Open-Source Variante Code-OSS) und [Remote-Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)-Extension installieren
- Dieses Repository klonen
- In VS-Code öffnen
- Auf die Meldung "Reopen in Container" klicken
- Falls die Meldung nicht angezeigt werden sollte, kann der Container auch über die Command Palette (F1) geöffnet werden: `Remote-Containers: Reopen in Container`
### Manuelle Installation (nicht empfohlen, aufwendig)
- Latex-Installation (z.B. MikTex oder TexLive)
- Installation der [TU-Template](https://github.com/tudace/tuda_latex_templates) und der verwendeten Plugins (inklusive Logo!)
- Installation der [AlgoTeX-Vorlage](https://github.com/TUDalgo/AlgoTeX#algotex---die-latex-vorlage-der-fop-und-aud)

## Formatieren
### Automatisch mit pre-commit hook
Der Pre-commit Hook formatiert die Dateien automatisch, bevor sie committet werden. Dieser Hook wird auch für die CI verwendet, um sicherzustellen, dass die Dateien immer formatiert sind.

um dem Pre-commit Hook zu verwenden, muss das python package `pre-commit` installiert werden. (siehe [Anleitung von Pre-commit](https://pre-commit.com/#install))
```sh
pip install pre-commit
```

> Hinweis: Auf manchen Linux-Distributionen, die python-Pakete nicht über pip installieren, sollte das Paket `pre-commit` bzw. `python3-pre-commit` über den Paketmanager installiert werden.

Dann kann der Pre-commit Hook mit folgendem Befehl installiert werden:
```sh
pre-commit install
```
Der Pre-commit Hook wird nun bei jedem Commit ausgeführt und formatiert die Dateien automatisch.

Falls der Pre-commit Hook unabhängig von einem Commit ausgeführt werden soll, kann er mit folgendem Befehl manuell ausgeführt werden:
```sh
pre-commit run -a
```

### Manuell mit latexindent
> Hinweis: Wenn VS-Code verwendet wird (mit oder ohne devcontainer), sollten die korrekten Einstellungen automatisch geladen werden, sofern die empfohlenen Extensions installiert sind.

Um eine einheitliche Formatierung zu gewährleisten, muss Latexindent installiert und entsprechend konfiguriert werden, um die mitgelieferte [`latexindent.yaml`](latexindent.yaml) zu verwenden.
Ein Aufruf von latexindent könnte z.B. so aussehen:
```sh
latexindent.pl -l -w myfile.tex
```
in `VS-Code` mit LaTeX-Workshop kann man die Folgende Konfiguration verwenden:

```json
"latex-workshop.latexindent.args": [
    "-c",
    "%DIR%/",
    "%TMPFILE%",
    "-l=%WORKSPACE_FOLDER%/latexindent.yaml",
    // "-m", // -m can have undesired sideeffects
    "-y=defaultIndent: '%INDENT%'"
],
```

Alternativ kann die Datei `defaultSettings.yaml` mit der mitgelieferten [`latexindent.yaml`](latexindent.yaml) überschrieben werden. Den Speicherort der Default Settings findet man über:
```sh
latexindent -vv
```

## Kompilieren
### Automatisch mit IDE (empfohlen)
Die meisten LaTeX-Editoren bieten eine Möglichkeit, die Materialien automatisch zu kompilieren. In VS-Code kann dies z.B. mit der LaTeX-Workshop-Extension erreicht werden.
### Automatisch mit make
Die Materialien können IDE-Unabhängig mit dem Befehl `make -j` kompiliert werden. Der Parameter `-j` sorgt dafür, dass die Datei parallel kompiliert wird, was die Kompilierzeit verkürzt. Dabei werden die folgenden Versionen erstellt:
- light mode
- dark mode
- light mode ohne sichtbare Punktzahlen (für Reviewer)
- dark mode ohne sichtbare Punktzahlen (für Reviewer)
### Automatisch mit act
Falls **genau** die gleiche Umgebung wie in der CI benötigt wird, kann `act` verwendet werden. Act nutzt Docker, um die CI-Umgebung lokal zu simulieren. Dann kann der Build mit folgendem Befehl ausgeführt werden:
```sh
act -j build --artifact-server-path /tmp/artifacts
```
Die erstellten PDFs werden dann im Ordner `/tmp/artifacts` abgelegt. (bei Bedarf kann der Pfad angepasst werden)

### Manuell mit Docker
Falls die lokale Installation von LaTeX nicht gewünscht ist, können die Materialien auch mit Docker kompiliert werden. Der Befehl könnte z.B. so aussehen:
```sh
docker run --rm -v $(pwd):/workspace -w /workspace ghcr.io/tudalgo/algotex:latest make -j $(nproc)
```

## Spell checking
Für Spell checking mit VS-Code empfehlen wir LTex, eine entsprechende Konfiguration ist vorgegeben.

LTex ist standardmäßig auf Deutsch eingestellt. Wenn ein englischer Abschnitt geprüft werden soll, kann die Sprache dafür temporär auf Englisch gestellt werden:
```latex
% Deutscher Text
Das ist ein Test
\begin{otherlanguage}{english}
    % Englischer Text
    This is a test.
\end{otherlanguage}
```

## Empfehlungen für LaTeX-Distribution und -Editoren
- Empfohlener Compiler: [`latexmk`](https://ctan.org/pkg/latexmk?lang=de) mit [`LuaLaTeX`](http://www.luatex.org/)
- Empfohlene LaTeX-Distribution: [`TeX-Live`](https://www.tug.org/texlive/)
- Auflistung der Empfohlenen LaTeX-Editoren:
    - [VS-Code](https://code.visualstudio.com/) (oder die Open-Source Variante Code-OSS) mit [LaTeX-Workshop](https://github.com/James-Yu/LaTeX-Workshop)-Extension
    - [Neovim](https://neovim.io/) mit [VimTeX](https://github.com/lervag/vimtex)-Plugin
    - [IntelliJ Idea](https://www.jetbrains.com/de-de/idea/) mit [TeXiFy IDEA](https://plugins.jetbrains.com/plugin/9473-texify-idea)-Plugin
    - [TeX-Studio](https://www.texstudio.org/)
- Hinweise für das Auswählen von PDF-Viewern:
    - Ein guter PDF-Viewer sollte synctex unterstützen, sodass man zwischen Quellcode und PDF hin- und her springen kann

## Lizenz
Eine Verwendung der Logos der Fachschaft Informatik, TU Darmstadt in (`lecture/globalMedia/*.(pdf|svg)`), ist nur für Fachschaftstätigkeiten gestattet.  

Alle anderen Inhalte dieses Projekts stehen, sofern nicht anders angegeben, unter der GNU General Public License v3.0 (GNU GPLv3):  

```
Copyright (C) 2019  Fachschaft Informatik Technische Universität Darmstadt

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

## Mithelfen
Wir freuen uns über jede Mithilfe, gerne auch für die Behebung von Rechtschreib- und Grammatikfehlern! Für kleinere Änderungen kann gerne ein Pull Request eingereicht werden. Bei größeren Änderungen kann ein Issue erst einmal sinnvoller sein, damit darüber diskutiert werden kann.  
  
Bei Interesse an der Organisation des Programmiervorkurses schreib uns gerne eine E-Mail!

### Git-Workflow
Für alle größeren Änderungen sollte ein neuer Feature-Branch erstellt werden, der dann durch einen PR in den `main`-Branch gemerged wird. Dabei werden die Commits des Feature-Branches in einem Squash-Merge zusammengefasst, sodass die Historie des `main`-Branches übersichtlich bleibt. Feature branches werden nach dem Mergen automatisch gelöscht.
