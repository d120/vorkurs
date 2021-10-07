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


def randint(minimum, maximum):
    """
    The Function generates a pseudo random Integer between (including) min and max

    Parameters:
        min(int): the Minimum
        max(int): the Maximum

    Returns:
        int: the random Number
    """
    # Global wurde nicht eingeführt, wenn man das nicht verwenden wil,
    # kann man randomindex einfach als Parameter übergeben
    global randomindex
    randomindex = randomindex + 1
    randomindex = randomindex % len(randomints)
    rand_range = maximum-minimum
    # Trim to given Range
    random = randomints[randomindex]
    random = random % (rand_range + 1)
    random = random + minimum
    return random


def getMaxStringLength(state):
    """
    Gets the length of the longest string in a two dimensional array

    Parameters:
        state(list): the 2d array

    Returns:
        int: the length of the longest string in the array
    """
    longest = 0
    for row in state:
        for field in row:
            if longest < len(str(field)):
                longest = len(str(field))
    return longest


def printField(state):
    """
    Prints the Game Field

    Parameters:
        state(list): the 2d array
    """
    longestString = getMaxStringLength(state)
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


def printGameState(state, game_round):
    """
    Prints the Information for a game_round of Playing

    Parameters:
        state(list): the 2d array
        game_round(int): the game_round number
    """
    print("Zug: " + str(game_round))
    maxTile = 0
    for row in state:
        for field in row:
            if maxTile < field:
                maxTile = field
    print("Höchster Wert: " + str(maxTile))
    printField(state)


def getNextMove():
    """
    Asks the User to input the next Move

    Returns: 
        list: a vector pointing in the desired direction with length one

    Throws: 
        SyntaxError: if the input is not a valid direction
    """
    move = input("\nNächster Zug (a=links,s=unten,w=oben,d=rechts):")

    # Info: In meiner Implementierung liegt die (0,0)-Koordinate in der oberen linken Ecke (nord west)
    # Also muss anders als vielleicht aus der Schulmathematik bekannt für "down" y verringert werden

    # Anmerkung: in diesem Fall Kann auch nur if statt elif verwendet werden (Short Circuit evaluation)

    # left
    if move == "a":
        return [-1, 0]
    # down
    elif move == "s":
        return [0, 1]
    # up
    elif move == "w":
        return [0, -1]
    # right
    elif move == "d":
        return [1, 0]
    else:
        print("Expected one of: [a, s, w, d] but got "+move+".")
        return getNextMove()


def hasEmptySlots(state):
    """
    Checks wheather the board has empty slots

    Parameters:
        state(list): the Current Game State

    Returns:
        boolean: true if empty slots exist
    """
    for y in range(4):
        for x in range(4):
            if(state[y][x] == 0):
                return True
    return False


def has2048(state):
    """
    Checks wheather the board has a 2048 Tile (win condition)

    Parameters:
        state(list): the Current Game State

    Returns:
        boolean: true if the board has a 2048 Tile
    """
    for row in state:
        for field in row:
            if field == 2048:
                return True
    return False


def pointIsInGameField(size, xPos, yPos):
    """
    Checks wheather a Cooardinate lies within the boundaries of the Board

    Parameters:
        size(int): the size of the Board

    Returns:
        boolean: true if the point lies within the boundaries of the Board
    """
    return xPos >= 0 and xPos < size and yPos >= 0 and yPos < size

### Gameplay Functions ###


def spawnNewTile(state):
    """
    Spawns a new Tile at a random free spot with value 2 or 4

    Parameters:
        state(list): the Current Game State

    Returns: 
        list: The new Game State
    """
    newState = state

    if hasEmptySlots(state):
        # Position
        newX = randint(0, 3)
        newY = randint(0, 3)
        # Get new Position until we find a free one (for better approach see advanced solution)
        while not state[newY][newX] == 0:
            newX = randint(0, 3)
            newY = randint(0, 3)
        # The weighted probability approach can be found in the advanced solution
        newValue = randint(1, 2)
        newState[newY][newX] = 2 * newValue
    return newState


def newGameState():
    """
    Creates a new Game State with two ramdom Tiles

    Returns: 
        list: The new Game State
    """
    newState = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    newState = spawnNewTile(newState)
    newState = spawnNewTile(newState)
    return newState


def slideTiles(currentState, xMov, yMov):
    """
    Slides all Tiles in a given direction

    Parameters:
        state(list): the Current Game State
        xMov(int): the X-Coordinate of the direction to move
        yMov(int): the Y-Coordinate of the direction to move

    Returns: 
        list: The new Game State

    Throws:
        ValueError: if the Direction is invalid
    """
    newState = currentState
    forwardRange = range(len(currentState))
    backwardRange = range(len(currentState)-1, -1, -1)
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
            field = currentState[y][x]
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
                nextX = newX+xMov
                nextY = newY+yMov
                if not pointIsInGameField(len(currentState), nextX, nextY):
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
    return newState


def main():
    """
    Starts a game of 2048
    """
    # Erste Runde
    state = newGameState()
    game_round = 1
    printGameState(state, game_round)
    # Weitere Runden
    while(True):
        direction = getNextMove()
        xMov = direction[0]
        yMov = direction[1]
        game_round = game_round + 1
        state = slideTiles(state, xMov, yMov)
        # loose scenario
        if not hasEmptySlots(state):
            print("You lost, there are no free spots left :(")
            break
        state = spawnNewTile(state)
        printGameState(state, game_round)
        # Win scenario
        if has2048(state):
            print("Congratulations, you won the Game :D")
            break


# def testRandomIntFunction():
#     nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     for i in range(0, 10000):
#         nums[randint(1, 10)-1] += 1
#     print(nums)
# testRandomIntFunction()


# Start the Game when launching the file
main()
