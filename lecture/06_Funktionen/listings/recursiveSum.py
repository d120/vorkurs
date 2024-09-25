def sum(wert):
    if (wert <= 0):
        return 0
    return wert + sum(wert - 1)

print(sum(20))
