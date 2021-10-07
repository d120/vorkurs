"""
Coding Challenge WS 21/22

██████╗░░█████╗░░░██╗██╗░█████╗░
╚════██╗██╔══██╗░██╔╝██║██╔══██╗
░░███╔═╝██║░░██║██╔╝░██║╚█████╔╝
██╔══╝░░██║░░██║███████║██╔══██╗
███████╗╚█████╔╝╚════██║╚█████╔╝
╚══════╝░╚════╝░░░░░░╚═╝░╚════╝░

~Regular Solution~

Created By Ruben Deisenroth in 2021
"""

randomindex = -1
# 100 zufallszahlen
randomints = [
    28, 9,  40, 74, 28, 56, 82, 61, 80, 95,
    14, 97, 47, 83, 63, 88, 91, 39, 2,  85,
    82, 61, 69, 35, 19, 17, 64, 21, 29, 20,
    94, 59, 73, 50, 1,  69, 30, 39, 26, 11,
    21, 94, 1,  24, 12, 8,  3,  90, 13, 8,
    52, 48, 41, 86, 60, 33, 74, 83, 9,  48,
    90, 12, 60, 44, 9,  58, 64, 61, 50, 74,
    97, 77, 69, 81, 62, 18, 22, 64, 25, 61,
    56, 63, 95, 39, 21, 6,  87, 98, 28, 52,
    35, 69, 43, 92, 94, 88, 4,  39, 6,  20
]


# Start the Game when launching the file


# First Round
newState = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# Spawn two tiles randomly
for counter in range(2):
    state = newState
    # Position
    randomindex += 1
    randomindex %= len(randomints)
    newX = randomints[randomindex] % 4
    randomindex += 1
    randomindex %= len(randomints)
    newY = randomints[randomindex] % 4

    # Get new Position until we find a free one (for better approach see advanced solution)
    while not state[newY][newX] == 0:
        randomindex += 1
        randomindex %= len(randomints)
        newX = randomints[randomindex] % 4
        randomindex += 1
        randomindex %= len(randomints)
        newY = randomints[randomindex] % 4
    # (The weighted probability approach can be found in the advanced solution)
    randomindex += 1
    randomindex %= len(randomints)
    newValue = randomints[randomindex] % 2
    newValue += 1
    newState[newY][newX] = 2 * newValue
state = newState
game_round = 1


# Print the Information for the first Round
print("Zug: " + str(game_round))
maxTile = 0
for row in state:
    for field in row:
        if maxTile < field:
            maxTile = field
print("Höchster Wert: " + str(maxTile))
# get maximum String length
longestString = 0
for row in state:
    for field in row:
        if longestString < len(str(field)):
            longestString = len(str(field))
trennzeile = "+"
for i in range(4):
    for k in range(longestString):
        trennzeile += "-"
    trennzeile += "+"
print(trennzeile)
for i in state:
    feldzeile = "|"
    for j in i:
        feldzeile += str(j)
        # Right Padding with space
        for k in range(longestString-len(str(j))):
            feldzeile += " "
        feldzeile += "|"
    print(feldzeile)
    print(trennzeile)


# Game Rounds
while(True):
    # Ask the User to input the next Move
    move = input("\nNächster Zug (a=links,s=unten,w=oben,d=rechts):")

    # Info: In meiner Implementierung liegt die (0,0)-Koordinate in der oberen linken Ecke (nord west)
    # Also muss anders als vielleicht aus der Schulmathematik bekannt für "down" y verringert werden

    # Anmerkung: in diesem Fall Kann auch nur if statt elif verwendet werden (Short Circuit evaluation)

    # left
    if move == "a":
        direction = [-1, 0]
    # down
    elif move == "s":
        direction = [0, 1]
    # up
    elif move == "w":
        direction = [0, -1]
    # right
    elif move == "d":
        direction = [1, 0]
    else:
        print("Expected one of: [a, s, w, d] but got " + move + ".")
        continue
    xMov = direction[0]
    yMov = direction[1]
    game_round = game_round + 1

    # Slide all Tiles in the given direction
    newState = state
    forwardRange = range(len(state))
    backwardRange = range(len(state) - 1, -1, -1)

    # Durch Feld Iterieren
    # Anmerkung: Hier muss man darauf achten, in welcher Reihenfolge man durch die Felder geht,
    # da sonst mehrere Felder auf einmal addiert werden können
    yrange = forwardRange
    xrange = forwardRange
    if yMov == 1:
        yrange = backwardRange
    if xMov == 1:
        xrange = forwardRange
    for y in yrange:
        for x in xrange:
            field = state[y][x]
            # Wenn das Feld leer ist, müssen wir nichts verschieben
            if(field == ''):
                continue
            # Neue Position Ermitteln
            newX = x
            newY = y

            # Ansatz: wir gehen solange in die gewünschte Richtung,
            # bis der nächste Schritt außerhalb des Feldes Läge oder wir auf ein nichtleeres Feld stoßen.
            # Sollten wir auf ein nichtleeres Feld mit dem Gleichen Wert stoßen, müssen wir den Wert des Feldes verdoppeln.
            for i in range(4):
                nextX = newX + xMov
                nextY = newY + yMov
                # Check whether a Cooardinate lies within the boundaries of the Board
                pointIsInGameField = nextX >= 0 and nextX < len(
                    state) and nextY >= 0 and nextY < len(state)
                if not pointIsInGameField:
                    break
                if newState[nextY][nextX] != 0:
                    if newState[nextY][nextX] == field:
                        newX = nextX
                        newY = nextY
                    break
                newX = nextX
                newY = nextY

            # Verschieben an neue Position, und ggf multiplizieren
            newState[y][x] = 0
            if(newState[newY][newX] != 0):
                newState[newY][newX] = newState[newY][newX] * 2
            else:
                newState[newY][newX] = field
    state = newState

    # check if player loses scenario
    noEmptySlots = True
    for y in range(4):
        for x in range(4):
            if(state[y][x] == 0):
                noEmptySlots = False
    if noEmptySlots:
        print("You lost, there are no free spots left :(")
        break
    newState = state

    # Spawns a new Tile at a random free spot with value 2 or 4
    hasEmptySlots = False
    for y in range(4):
        for x in range(4):
            if(state[y][x] == 0):
                hasEmptySlots = True
    if hasEmptySlots:
        # Position
        randomindex += 1
        randomindex %= len(randomints)
        newX = randomints[randomindex] % 4
        randomindex += 1
        randomindex %= len(randomints)
        newY = randomints[randomindex] % 4

        # Get new Position until we find a free one (for better approach see advanced solution)
        while not state[newY][newX] == 0:
            randomindex += 1
            randomindex %= len(randomints)
            newX = randomints[randomindex] % 4
            randomindex += 1
            randomindex %= len(randomints)
            newY = randomints[randomindex] % 4
        randomindex += 1
        randomindex %= len(randomints)
        newValue = randomints[randomindex] % 2
        newValue += 1
        newState[newY][newX] = 2 * newValue
    state = newState

    # Print the Information for the current Round
    print("Zug: " + str(game_round))
    maxTile = 0
    for row in state:
        for field in row:
            if maxTile < field:
                maxTile = field
    print("Höchster Wert: " + str(maxTile))

    # get maximum String length
    longestString = 0
    for row in state:
        for field in row:
            if longestString < len(str(field)):
                longestString = len(str(field))
    trennzeile = "+"
    for i in range(4):
        for k in range(longestString):
            trennzeile += "-"
        trennzeile += "+"
    print(trennzeile)
    for i in state:
        feldzeile = "|"
        for j in i:
            feldzeile += str(j)
            # Right Padding with space
            for k in range(longestString-len(str(j))):
                feldzeile += " "
            feldzeile += "|"
        print(feldzeile)
        print(trennzeile)

    # Check if player wins
    has2048 = False
    for row in state:
        for field in row:
            if field == 2048:
                has2048 = True
    if has2048:
        print("Congratulations, you won the Game :D")
        break
