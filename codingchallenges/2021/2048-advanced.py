"""
Coding Challenge WS 21/22

██████╗░░█████╗░░░██╗██╗░█████╗░
╚════██╗██╔══██╗░██╔╝██║██╔══██╗
░░███╔═╝██║░░██║██╔╝░██║╚█████╔╝
██╔══╝░░██║░░██║███████║██╔══██╗
███████╗╚█████╔╝╚════██║╚█████╔╝
╚══════╝░╚════╝░░░░░░╚═╝░╚════╝░

~Advanced Solution~

Created By Ruben Deisenroth in 2021
"""


### Variable Definitions ###

# The Possible Directions
directions = {
    "a": "left",
    "s": "down",
    "w": "up",
    "d": "right"
}

# Info: In meiner Implementierung liegt die (0,0)-Koordinate in der oberen linken Ecke (nord west)
# Also muss anders als vielleicht aus der Schulmathematik bekannt für "down" y verringert werden

# Translate direction to a vector with length 1 [x, y]
directionVectors = {
    "left":  [-1, 0],
    "down":  [0,  1],
    "up":    [0, -1],
    "right": [1,  0],
}


x = 69
y = 420
z = 1337
w = 2021

### Helper Functions ###

# https://en.wikipedia.org/wiki/Xorshift


def randint(minimum: int, maximum: int):
    """
    The Function generates a pseudo random Integer between (including) min and max

    Parameters:
        min(int): the Minimum
        max(int): the Maximum

    Returns: 
        int: the random Number
    """
    global x, y, z, w
    t = x ^ ((x << 11) & 0xFFFFFFFF)  # 32bit
    x, y, z = y, z, w
    w = (w ^ (w >> 19)) ^ (t ^ (t >> 8))
    return (w % (maximum-minimum+1)) + minimum


def getMaxStringLength(state: list):
    """
    Gets the length of the longest string in a two dimensional array

    Parameters:
        state(list): the 2d array

    Returns: 
        int: the length of the longest string in the array
    """
    return len(str(max(map(lambda x: max(x, key=lambda y: len(str(y))), state), key=lambda x: len(str(x)))))


def printField(state: list):
    """
    Prints the Game Field

    Parameters:
        state(list): the 2d array
    """
    # Add two spaces for stylistic reasons
    maxLength = getMaxStringLength(state)+2
    hline = f"+{('-' * maxLength+'+')*len(state)}"
    print(hline, end='')
    for row in state:
        print(
            f"\n|{'|'.join(map(lambda x: str(x).center(maxLength),row))}|\n{hline}", end='')


def printGameState(state: list, round: int):
    """
    Prints the Information for a Round of Playing

    Parameters:
        state(list): the 2d array
        round(int): the round number
    """
    print(f"Zug: {round}")
    print(
        f"Höchster Wert: {max(map(lambda x : max(map(lambda y : y if isinstance(y,int) else 0, x)),state))}")
    printField(state)


def getNextMove():
    """
    Asks the User to input the next Move

    Returns: 
        string: the chosen direction

    Throws: 
        SyntaxError: if the input is not a valid direction
    """
    move = input("\nNächster Zug (a=links,s=unten,w=oben,d=rechts):")
    if not move in directions:
        print(
            f"Expected one of: [{', '.join(directions.keys())}] but got {move}.")
        return getNextMove()
    return directions.get(move)


def getEmptySlots(state):
    """
    Collects all the Empty Slots of a game State

    Parameters:
        state(list): the Current Game State

    Returns:
        list: a list of Coordinates of the empty Slots [x,y]
    """
    slots = []
    for y in range(len(state)):
        for x in range(len(state[y])):
            if(state[y][x] == ''):
                slots.append([x, y])
    return slots


def hasEmptySlots(state):
    """
    Checks wheather the board has empty slots

    Parameters:
        state(list): the Current Game State

    Returns:
        boolean: true if empty slots exist
    """
    return len(getEmptySlots(state)) > 0


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


def pointIsInGameField(size: int, xPos: int, yPos: int):
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
    emptySlots = getEmptySlots(state)
    if(len(emptySlots) > 0):
        [newX, newY] = emptySlots[randint(0, len(emptySlots)-1)]
        newState[newY][newX] = 4 if randint(1, 10) == 10 else 2
    return newState


def newGameState():
    """
    Creates a new Game State with two ramdom Tiles

    Returns: 
        list: The new Game State
    """
    newState = [['', '', '', ''], ['', '', '', ''],
                ['', '', '', ''], ['', '', '', '']]
    newState = spawnNewTile(newState)
    newState = spawnNewTile(newState)
    return newState


def slideTiles(currentState: list, direction: str):
    """
    Slides all Tiles in a given direction

    Parameters:
        state(list): the Current Game State
        direction(str): the direction to move

    Returns: 
        list: The new Game State

    Throws:
        ValueError: if the Direction is invalid
    """
    if not direction in directions.values():
        raise ValueError(
            f"Direction must be one of: [{', '.join(directions.values())}] but got {direction}.")
    newState = currentState
    [xMov, yMov] = directionVectors.get(direction)
    forwardRange = range(len(currentState))
    backwardRange = range(len(currentState)-1, -1, -1)
    # Durch Feld Iterieren
    # Anmerkung: Hier muss man darauf achten, in welcher Reihenfolge man durch die Felder geht,
    # da sonst mehrere Felder auf einmal addiert werden können
    for y in backwardRange if yMov == 1 else forwardRange:
        for x in backwardRange if xMov == 1 else forwardRange:
            field = currentState[y][x]
            # Wenn das Feld leer ist, müssen wir nichts verschieben
            if(field == ''):
                continue
            # Neue Position Ermitteln
            newPos = [x, y]
            # Ansatz: wir gehen solange in die gewünschte Richtung,
            # bis der nächste Schritt außerhalb des Feldes Läge oder wir auf ein nichtleeres Feld stoßen.
            # Sollten wir auf ein nichtleeres Feld mit dem Gleichen Wert stoßen, müssen wir den Wert des Feldes verdoppeln.
            for i in range(len(currentState)):
                nextPos = [newPos[0]+xMov, newPos[1]+yMov]
                [nextX, nextY] = nextPos
                if not pointIsInGameField(len(currentState), nextX, nextY):
                    break
                if newState[nextY][nextX] != '':
                    if newState[nextY][nextX] == field:
                        newPos = nextPos
                    break
                newPos = nextPos
            [newX, newY] = newPos
            # Verschieben an neue Position, und ggf multiplizieren
            newState[y][x] = ''
            if(newState[newY][newX] != ''):
                newState[newY][newX] += field
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
        # clear Console Output every round
        print("\033[H\033[J", end="")
        game_round += 1
        state = slideTiles(state, direction)
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
#     nums = [0,0,0,0,0,0,0,0,0,0]
#     for i in range(0,10000):
#         nums[randint(1,10)-1]+=1
#     print(nums)


# Start the Game when launching the file
main()
