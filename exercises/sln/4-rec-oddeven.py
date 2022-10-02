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


print(f"even(42)= {even(42)}")
print(f"odd(42)= {odd(42)}")
print(f"even(23)= {even(23)}")
print(f"odd(23)= {odd(23)}")
