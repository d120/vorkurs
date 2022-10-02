a = int(input("Zahl a einlesen: "))
b = int(input("Zahl b einlesen: "))
c = int(input("Zahl c einlesen: "))
d = 2 * a
a = d + 3
d = int(input("Zahl d einlesen: "))
print(b)
print(c)
c = a > d
if c:
    d = a
c = a < d
if c:
    c = d - a
b = a * a
a = b
b = c * d
c = a + b
a = c
b = a + d
c = b + d
print(a)
print(b)
print(c)
print(d)
