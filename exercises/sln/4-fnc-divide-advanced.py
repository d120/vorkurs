def stepwiseDivision(dividend, divisor):
    quotient = str(dividend // divisor)
    remainder = dividend % divisor
    if remainder == 0:
        return quotient

    decimals = ""
    position = 0
    remainders = [0] * divisor
    isPeriodic = False
    while remainder != 0 and not isPeriodic:
        position += 1
        if remainders[remainder] == 0:
            remainders[remainder] = position
            decimals += str(remainder * 10 // divisor)
            remainder = remainder * 10 % divisor
        else:
            isPeriodic = True
            position = remainders[remainder] - 1
            decimals = "{}({})".format(
                decimals[0:position], decimals[position:])
    return f"{quotient},{decimals}"


dividend = int(input("Dividend: "))
divisor = int(input("Divisor: "))

quotient = stepwiseDivision(dividend, divisor)
print("Quotient: " + quotient)
