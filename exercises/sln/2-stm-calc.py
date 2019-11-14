#!/usr/bin/env python3
op1 = int(input("Wie lautet der erste Operand: "))
op2 = int(input("Wie lautet der zweite Operand: "))
op = input("Wie lautet der Operator: ")

if op == "+":
	print("Das Ergebnis lautet:", op1 + op2)
elif op == "-":
	print("Das Ergebnis lautet:", op1 - op2)
elif op == "*":
	print("Das Ergebnis lautet:", op1 * op2)
elif op == "/":
	print("Das Ergebnis lautet:", op1 / op2)
else:
	print("Keine gültige Eingabe!")
