
def plus(op1, op2):
    return op1 + op2


def minus(op1, op2):
    return op1 - op2


def mal(op1, op2):
    return op1 * op2


def teilen(op1, op2):
    return op1 / op2


def potenz(op1, op2):
    return op1 ** op2


op1 = float(input("Wie lautet der erste Operand: "))
op2 = float(input("Wie lautet der zweite Operand: "))
op = input("Wie lautet der Operator: ")
if op == "+":
    print("Das Ergebnis lautet: " + str(plus(op1, op2)))
elif op == "-":
    print("Das Ergebnis lautet: " + str(minus(op1, op2)))
elif op == "*":
    print("Das Ergebnis lautet: " + str(mal(op1, op2)))
elif op == "/":
    print("Das Ergebnis lautet: " + str(teilen(op1, op2)))
elif op == "^":
    print("Das Ergebnis lautet: " + str(potenz(op1, op2)))
else:
    print("Keine gueltige Eingabe!")
