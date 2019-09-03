# Vorlesungsfolien

## Kompilierung
Über ein `make` werden **alle** Vorlesungsfolien erzeugt und in den `pdfout`-Ordner kopiert. Das Makefile akzeptiert verschiedene Optionen:

* Auch nur einzelne Foliensätze können erzeugt werden: `make <subfolder>/<file>.tex`. Zum Beispiel: `make 01_Einfuehrung/01_Einfuehrung.tex`.
* Über die Umgebungsvariable `VORKURS_NOTES` lässt sich die Erzeugung der geteilten Presenter-Ansicht (Folie links, Notizen rechts) steuern. Zum Beispiel erzeugt  `VORKURS_NOTES=1 make 01_Einfuehrung/01_Einfuehrung.tex` den ersten Foliensatz in der Presenter-Ansicht.
