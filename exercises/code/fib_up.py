def fib_normal(n: int):
    a: int = 0
    b: int = 1
    for _ in range(n):
        print(b, end=", ")
        tmp = b
        b = a + b
        a = tmp
    print()

fib_normal(10)

x = "1"
x_int = int(input())

x: str = input()
y: str = input()

def mod(a: int, b:int):
    return a % b


if x % 2 == 0:
    ...

elif x % 3 == 0:
    ...

elif x % 4 == 0:
    ...


