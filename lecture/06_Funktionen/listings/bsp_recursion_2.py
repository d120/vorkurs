def fibonacci(x):
    if (x == 0 or x == 1): # Rekursionsanker
        return 1
    else: # Rekursionsaufruf:
        return fibonacci(x-1) + fibonacci(x-2)
