def fib_normal(n: int):
    elements = [0, 1]
    for i in range(n):
        elements.append(elements[i] + elements[i + 1])

    for i in range(n):
        # Man beachte hier das Element an der Stelle 0 wird hier nicht ausgegeben da n-i minimal 1 werden kann
        print(elements[n - i])

fib_normal(10)
