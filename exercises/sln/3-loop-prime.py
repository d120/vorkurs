prim = int(input("Gib bitte eine Zahl ein: "))
isPrim = True

for i in range(2, prim)
	if(prim % i == 0):
		isPrim = false
		break

if isPrim:
	print("{0} ist eine Primzahl!".format(prim))
else:
	print("{0} ist keine Primzahl!".format(prim))
