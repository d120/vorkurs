def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = 1

    finished = False
    while not finished:
        placed = False
        while not placed:
            printBoard(board)
            print("Spieler " + getChar(player) + " ist am Zug...")
            x = input("x: ")
            y = input("y: ")

            if int(x) < 1 or int(x) > 3 or int(y) < 1 or int(y) > 3:
                print("Feld ist außerhalb des Spielfeldes")
            elif board[int(y) - 1][int(x) - 1] != 0:
                print("Feld ist schon besetzt.")
            else:
                placed = True

        board[int(y) - 1][int(x) - 1] = player
        printBoard(board)
        if checkWin(board, player):
            print("Spieler " + getChar(player) + " hat gewonnen!")
            finished = True
        elif checkDraw(board):
            print("Die Runde ist unentschieden.")
            finished = True

        if player == 1:
            player = 2
        else:
            player = 1


def checkWin(board, player):
    for i in range(3):
        row = board[i]
        col = [board[0][i], board[1][i], board[2][i]]
        if row[0] == row[1] == row[2] == player:
            return True
        if col[0] == col[1] == col[2] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def checkDraw(board):
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True

def printBoard(board):
    print()
    print("+-+-+-+")
    for row in board:
        print("|" + getChar(row[0]) + "|" + getChar(row[1]) + "|" + getChar(row[2]) + "|")
        print("+-+-+-+")

def getChar(state):
    if state == 0:
        return " "
    if state == 1:
        return "X"
    return "O"

main()
