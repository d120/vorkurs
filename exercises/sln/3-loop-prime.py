prime = int(input("Gib bitte eine Zahl ein: "))
is_prime = True

for i in range(2, prime):
    if prime % i == 0:
        is_prime = False
        break

if is_prime:
    print("{0} ist eine Primzahl!".format(prime))
else:
    print("{0} ist keine Primzahl!".format(prime))
