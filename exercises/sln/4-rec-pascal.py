def pascal(row, column):
    if row < 0 or column > row:
        return -1
    if column == 0 or column == row:
        return 1
    return pascal(row - 1, column - 1) + pascal(row - 1, column)


zeile = int(input("Zeile: "))
spalte = int(input("Spalte: "))
print(pascal(zeile, spalte))
