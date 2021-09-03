name = input("Bitte gib deinen Namen ein: ")
alter = input("Bitte gib dein Gewicht ein: ")
groesse = input("Bitte gib deine Größe ein: ")

print(name + " ist " + alter + " Jahre alt und " + groesse + "m groß.")

# Dies ist neu
alter = int(alter)
alter += 1
print(name + " ist nächstes Jahr " + str(alter) + " Jahre alt")
# Erklärung: alter ist noch ein String, also erst umwandeln in Zahl
# Zuerst ohne Konvertierung zeigen und erklären was passiert. Ebenfalls die Konvertierung von alter weglassen.
print(f"{name} ist nächstes Jahr {alter} Jahre alt")
# Das hier funktioniert übrigens, weil der format-String automatisch die Variablen in Strings konvertiert

groesse = float(groesse)
# Erklärung: groesse ist noch ein String, also erst umwandeln in Zahl
groesse_cm = groesse * 100
print(groesse + "m sind übrigens " + str(groesse_cm) + "cm")
