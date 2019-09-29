alter = int(input("Wie alt bist du? "))
antwort = input("Hast du die deutsche Staatsbürgerschaft? ")

if antwort == "j" or antwort == "J":
    deutsch = True

if alter >= 18 and deutsch:
    print("Du darfst am 28. Oktober 2018 wählen gehen.")
else:
    print("Nicht wahlberechtigt für die Landtagswahl.")

if (deutsch or not deutsch) and (alter + 5) >= 18:
    print("Du darfst bei der nächsten Kommunalwahl in 5 Jahren wählen gehen.")
# Erklärung: Jeder EU-Bürger wenn Hauptwohnsitz. Etwas vereinfacht.

# INFO: Später vereinfachen zu
if (alter + 5) >= 18:
    print("Du darfst bei der nächsten Kommunalwahl in 5 Jahren wählen gehen.")
