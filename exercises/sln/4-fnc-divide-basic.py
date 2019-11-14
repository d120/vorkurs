
def stepwiseDivision(dividend, divisor):
    quotient = str(dividend // divisor)
    remainder = dividend % divisor
    if remainder == 0:
        return quotient

    decimals = ""
    position = 0
    while remainder != 0:
        decimals += str(remainder * 10 // divisor)
        remainder = remainder * 10 % divisor
        position += 1
    return "{0},{1}".format(quotient, decimals)


dividend = int(input("Dividend: "))
divisor = int(input("Divisor: "))

quotient = stepwiseDivision(dividend, divisor)
print("Quotient: " + quotient)
