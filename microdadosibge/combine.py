from math import floor, log10, isnan

def combineToFloat(a, b):
    n = False
    if a < 0:
        n = True
        a = -a
    if b < 0:
        n = True
        b = -b
    elif b == 0:
        return a

    result = a + b * 10**-(floor(log10(b))+1)

    if n:
        return -result
    else:
        return result
