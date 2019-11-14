#!/usr/bin/python3
name = input("Bitte gib deinen Namen ein: ")
tag = int(input("Gib den Tag deiner Geburt ein: "))
monat = int(input("Gib den Monat deiner Geburt ein: "))
jahr = int(input("Gib das Jahr deiner Geburt ein: "))

print("{0} hat am {1}.{2}.{3} Geburtstag.".format(name, tag, monat, jahr))