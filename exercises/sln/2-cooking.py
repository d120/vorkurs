#!/usr/bin/env python3
Mehl = 450
Wasser = 250
Salz = 1
Oliven = 4
Backpulver = 2
Tomaten = 400
Oregano = 1
Knoblauch = 1
z = input("Zutat eingeben: ")
m = float(input("Menge eingeben (ohne Einheit): "))
Zutatenliste = "Zutatenliste: \n Mehl: {0} g \n Wasser: {1} ml \n Salz: {2} TL, gestrichen \n Olivenöl: {3} EL \n Backpulver: {4} TL \n passierte Tomaten: {5} g \n Oregano {6} EL \n Knoblauch {7} Zehe(n)"
if z == "Mehl":
    factor = m / Mehl
    print(Zutatenliste.format(m, factor * Wasser, factor * Salz, factor * Oliven, factor * Backpulver, factor * Tomaten, factor * Oregano, factor * Knoblauch))
elif z == "Wasser":
    factor = m / Wasser
    print(Zutatenliste.format(factor * Mehl, m, factor * Salz, factor * Oliven, factor * Backpulver, factor * Tomaten, factor * Oregano, factor * Knoblauch))
elif z == "Salz":
    factor = m / Salz
    print(Zutatenliste.format(factor * Mehl, factor * Wasser, m, factor * Oliven, factor * Backpulver, factor * Tomaten, factor * Oregano, factor * Knoblauch))
elif z == "Olivenöl":
    factor = m / Oliven
    print(Zutatenliste.format(factor * Mehl, factor * Wasser, factor * Salz, m, factor * Backpulver, factor * Tomaten, factor * Oregano, factor * Knoblauch))
elif z == "Backpulver":
    factor = m / Backpulver
    print(Zutatenliste.format(factor * Mehl, factor * Wasser, factor * Salz, factor * Oliven, m, factor * Tomaten, factor * Oregano, factor * Knoblauch))
elif z == "Tomaten":
    factor = m / Tomaten
    print(Zutatenliste.format(factor * Mehl, factor * Wasser, factor * Salz, factor * Oliven, factor * Backpulver, m, factor * Oregano, factor * Knoblauch))
elif z == "Oregano":
    factor = m / Oregano
    print(Zutatenliste.format(factor * Mehl, factor * Wasser, factor * Salz, factor * Oliven, factor * Backpulver, factor * Tomaten, m, factor * Knoblauch))
elif z == "Knoblauch":
    factor = m / Knoblauch
    print(Zutatenliste.format(factor * Mehl, factor * Wasser, factor * Salz, factor * Oliven, factor * Backpulver, factor * Tomaten, factor * Oregano, m))
else:
    print("Eingabe nicht erkannt")
