def even(n):
    n = int(n)
    if n == 0:
        return True
    else:
        return odd(n - 1)


def odd(n):
    n = int(n)
    if n == 0:
        return False
    else:
        return even(n - 1)


print("even(42)= {}".format(even(42)))
print("odd(42)= {}".format(odd(42)))
print("even(23)= {}".format(even(23)))
print("odd(23)= {}".format(odd(23)))
