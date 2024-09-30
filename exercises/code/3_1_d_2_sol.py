prime: int = int(input("Gebe eine Zahl ein: "))

isPrime: bool = True
if prime <= 1:
    isPrime = False
else:
    for i in range(2, prime):
        if prime % i == 0:
            isPrime = False
            break

if isPrime:
    print(f"{prime} ist eine Primzahl.")
else:
    print(f"{prime} ist keine Primzahl.")
