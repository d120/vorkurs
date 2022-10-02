def plus(op1, op2):
    if op1 == 0:
        return op2
    elif op2 == 0:
        return op1
    else:
        return plus(op1 + 1, op2 - 1)


def minus(op1, op2):
    if op2 == 0:
        return op1
    else:
        return minus(op1 - 1, op2 - 1)


def mal(op1, op2):
    if op1 == 0 or op2 == 0:
        return 0
    else:
        return plus(mal(op1, minus(op2, 1)), op1)


def teilen(op1, op2):
    if op2 == 0:
        return -1
    elif op1 < op2:
        return 0
    else:
        return plus(teilen(minus(op1, op2), op2), 1)


def modulo(op1, op2):
    if op2 == 0:
        return -1
    elif op1 < op2:
        return op1
    else:
        return modulo(minus(op1, op2), op2)


def potenz(op1, op2):
    if op2 == 0:
        return 1
    else:
        return mal(potenz(op1, minus(op2, 1)), op1)


def ggT(op1, op2):
    if op1 == 0:
        return op2
    elif op2 == 0:
        return op1
    else:
        return ggT(op2, modulo(op1, op2))


def minimum(op1, op2):
    if op1 == 0 or op2 == 0:
        return 0
    else:
        return plus(minimum(minus(op1, 1), minus(op2, 1)), 1)


def maximum(op1, op2):
    if op1 == 0:
        return op2
    elif op2 == 0:
        return op1
    else:
        return plus(maximum(minus(op1, 1), minus(op2, 1)), 1)


op1 = int(input("Wie lautet der erste Operand: "))
op2 = int(input("Wie lautet der zweite Operand: "))
op = input("Wie lautet der Operator: ")
if op == "+":
    print(f"Das Ergebnis lautet: {plus(op1, op2)}")
elif op == "-":
    print(f"Das Ergebnis lautet: {minus(op1, op2)}")
elif op == "*":
    print(f"Das Ergebnis lautet: {mal(op1, op2)}")
elif op == "/":
    print(f"Das Ergebnis lautet: {teilen(op1, op2)}")
elif op == "%":
    print(f"Das Ergebnis lautet: {modulo(op1, op2)}")
elif op == "^":
    print(f"Das Ergebnis lautet: {potenz(op1, op2)}")
elif op == "T":
    print(f"Das Ergebnis lautet: {ggT(op1, op2)}")
elif op == "_":
    print(f"Das Ergebnis lautet: {minimum(op1, op2)}")
elif op == "|":
    print(f"Das Ergebnis lautet: {maximum(op1, op2)}")
else:
    print("Keine gültige Eingabe!")
