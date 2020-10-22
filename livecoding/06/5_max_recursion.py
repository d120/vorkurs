# 1. Simpler Fall: Ruft sich dauerhaft aus, ohne Ende!
def fn():
    fn()


# 2. fakultaet aus 4_recursion.py


def fakultaet(zahl):
    if zahl < 0:
        print("Falsche Eingabe")
        return False
    elif zahl <= 1:
        return 1
    else:
        return zahl * fakultaet(zahl - 1)


# max recursion:
print(fakultaet(1001))
