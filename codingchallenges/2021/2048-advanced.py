"""
Coding Challenge WS 21/22

██████╗░░█████╗░░░██╗██╗░█████╗░
╚════██╗██╔══██╗░██╔╝██║██╔══██╗
░░███╔═╝██║░░██║██╔╝░██║╚█████╔╝
██╔══╝░░██║░░██║███████║██╔══██╗
███████╗╚█████╔╝╚════██║╚█████╔╝
╚══════╝░╚════╝░░░░░░╚═╝░╚════╝░

~Advanced Solution~

Stand: 08.10. 23:34 Uhr

Created By Ruben Deisenroth in 2021
"""


### Variable Definitions ###

# The Possible Directions
directions = {
    "w": "up",
    "a": "left",
    "s": "down",
    "d": "right",
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

display_style = 1
color_new = False

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


def deepCopy(liste: list):
    """Returns a deep Copy of a given List

    Args:
        liste (list): The List to Create a deep Copy of

    Returns:
        list: The Deep Copy
    """
    neueListe = liste.copy()
    for i in range(len(liste)):
        if type(liste[i]) == list:
            neueListe[i] = deepCopy(liste[i])
    return neueListe


def getMaxStringLength(state: list):
    """
    Gets the length of the longest string in a two dimensional array

    Parameters:
        state(list): the 2d array

    Returns: 
        int: the length of the longest string in the array
    """
    return len(str(max(map(lambda x: max(x, key=lambda y: len(str(y))), state), key=lambda x: len(str(x)))))


def printField(state: list, style: int = 1, color_new: bool = False, new_fields: list = []):
    """Prints the Game Field

    Args:
        state (list): the 2d array
        style (int, optional): the Display Style (1=normal, 2=fancy). Defaults to 1.
        color_new (bool, optional): Whether to color new fields. Defaults to False.
        new_fields (list, optional): a list of coordinates(x,y) like:[[1,2],[2,3]]. Defaults to [].
    """
    # Add two spaces for stylistic reasons
    maxLength = getMaxStringLength(state)+2
    hlineupper = ""
    hlinelower = ""
    borderspacer = ""
    betweenspacer = ""
    if (style == 1):
        hlinelower = f"+{('-' * maxLength+'+')*len(state)}\n"
        print(hlinelower, end='')
        borderspacer = "|"
        betweenspacer = "|"
    else:
        hlineupper = f"{('╭'+ '-' * maxLength+'╮')*len(state)}\n"
        hlinelower = f"{('╰'+ '-' * maxLength+'╯')*len(state)}\n"
        borderspacer = "|"
        betweenspacer = "||"
    for y, row in enumerate(state):
        print(
            f"{hlineupper}"
            + f"{borderspacer}"
            + betweenspacer.join(
                map(lambda x:
                    ('\033[94m' if color_new and [x[0], y]
                        in new_fields else "")
                    + str(x[1]).center(maxLength)
                    + ('\033[0m' if color_new and [x[0], y]
                        in new_fields else ""),
                    enumerate(row))
            )
            + f"{borderspacer}"
            + f"\n{hlinelower}",
            end='')


def printGameState(state: list, game_round: int, new_fields: list = [[3, 0]]):
    """
    Prints the Information for a Round of Playing

    Parameters:
        state(list): the 2d array
        game_round(int): the game round number
    """
    # clear Previous Output
    print("\033[H\033[J\033[0m", end="")
    print(f"Zug: {game_round}")
    print(
        f"Höchster Wert: {max(map(lambda x : max(map(lambda y : y if isinstance(y,int) else 0, x)),state))}")
    printField(state, display_style, color_new, new_fields)


def getNextMove(state: list, game_round: int, new_fields: list = []):
    """
    Asks the User to input the next Move

    Returns: 
        string: the chosen direction

    Throws: 
        SyntaxError: if the input is not a valid direction
    """
    move = input("\nNächster Zug (w=oben,a=links,s=unten,d=rechts):").lower()
    global display_style, color_new
    if move == "exit" or move == "quit":
        print("bye")
        exit()
    # Eastereggs :D
    elif move == "plain":
        display_style = 1
        printGameState(state, game_round, new_fields)
        return getNextMove(state, game_round, new_fields)
    elif move == "fancy":
        display_style = 2
        printGameState(state, game_round, new_fields)
        return getNextMove(state, game_round, new_fields)
    elif move == "color":
        color_new = True
        printGameState(state, game_round, new_fields)
        return getNextMove(state, game_round, new_fields)
    elif move == "nocolor":
        color_new = False
        printGameState(state, game_round, new_fields)
        return getNextMove(state, game_round, new_fields)
    elif not move in directions:
        print(
            f"Expected one of: [{', '.join(directions.keys())}] but got {move}.")
        return getNextMove(state, game_round, new_fields)
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
            if (state[y][x] == ''):
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
    if (len(emptySlots) > 0):
        [newX, newY] = emptySlots[randint(0, len(emptySlots)-1)]
        newState[newY][newX] = 4 if randint(1, 10) == 10 else 2
    return newState


def newGameState():
    """
    Creates a new Game State with two ramdom Tiles

    Returns: 
        list: The new Game State
    """
    newState = [
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', '']]
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
    newState = deepCopy(currentState)
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
            if (field == ''):
                continue
            # Neue Schiebeposition Ermitteln
            newPos = [x, y]
            # Ansatz: wir gehen solange in die Schieberichtung,
            # bis der nächste Schritt außerhalb des Feldes Läge oder wir auf ein nichtleeres Feld stoßen.
            for i in range(len(currentState)):
                nextPos = [newPos[0]+xMov, newPos[1]+yMov]
                [nextX, nextY] = nextPos
                if not pointIsInGameField(len(currentState), nextX, nextY) or newState[nextY][nextX] != '':
                    break
                newPos = nextPos
            # Neue Verschmelzposition
            newMergePos = [x, y]
            # # Ansatz: wir gehen solange entgegen der Schieberichtung,
            # bis der nächste Schritt außerhalb des Feldes Läge oder wir auf ein nichtleeres Feld stoßen.
            # Sollten wir auf ein nichtleeres Feld mit dem Gleichen Wert stoßen, haben wir eine Verschmelzposition gefunden.
            for i in range(len(currentState)):
                prevPos = [newMergePos[0]-xMov, newMergePos[1]-yMov]
                [prevX, prevY] = prevPos
                if not pointIsInGameField(len(currentState), prevX, prevY):
                    break
                if newState[prevY][prevX] != '':
                    if newState[prevY][prevX] == field:
                        newMergePos = prevPos
                        break
                    break
                newMergePos = prevPos
            [newX, newY] = newPos
            [newMergeX, newMergeY] = newMergePos
            # Verschieben an neue Position, und ggf multiplizieren
            newState[y][x] = ''
            # Wenn das Feld an der Verschmelzposition nicht leer ist,
            # müssen wir den Wert des Feldes verdoppeln
            if (newState[newMergeY][newMergeX] != ''):
                newState[newY][newX] = field+newState[newMergeY][newMergeX]
                newState[newMergeY][newMergeX] = ''
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
    while (True):
        direction = getNextMove(state, game_round)
        game_round += 1
        state = slideTiles(state, direction)
        # loose scenario
        if not hasEmptySlots(state):
            print("You lost, there are no free spots left :(")
            break
        prevState = deepCopy(state)
        state = spawnNewTile(state)
        new_fields = []
        for y, row in enumerate(state):
            for x, field in enumerate(row):
                if prevState[y][x] != field:
                    new_fields.append([x, y])
        printGameState(state, game_round, new_fields)
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
