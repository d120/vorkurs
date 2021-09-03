name = input("Bitte gib deinen Namen ein: ")
alter = input("Bitte gib dein Gewicht ein: ")
groesse = input("Bitte gib deine Größe ein: ")

print(name + " ist " + alter + " Jahre alt und " + groesse + "m groß.")  # klobiger, doofer Python Syntax
print(f"{name} ist {alter} Jahre alt und {groesse}m groß.")  # fancy, cooler Python Syntax
print(groesse + "m sind übrigens " + groesse)
