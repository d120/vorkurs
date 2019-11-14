
def summe(werte):
    summe = 0
    for n in werte:
        summe += n
    return summe


def durchschnitt(werte):
    return summe(werte) / len(werte)


werte = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(summe(werte))
print(durchschnitt(werte))
