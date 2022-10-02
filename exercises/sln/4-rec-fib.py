def fib(n):
    n = int(n)
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 21):
    print(fib(i))
