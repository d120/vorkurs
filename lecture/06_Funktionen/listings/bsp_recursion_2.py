def fib(n):
    if (n < 2):  # Rekursionsanker
        return n

    # Rekursionsaufruf
    return fib(n - 1) + fib(n - 2)
