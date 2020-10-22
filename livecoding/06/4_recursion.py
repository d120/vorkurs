def fakultaet(zahl):
    if zahl < 0:
        print("Falsche Eingabe")
        return False
    elif zahl <= 1:
        return 1
    else:
        return zahl * fakultaet(zahl - 1)


print(fakultaet(-1))
print(fakultaet(0))
print(fakultaet(1))
print(fakultaet(3))
print(fakultaet(10))
