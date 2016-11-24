from math import floor, log10

def combineToFloat(a, b):
    if b == 0:
        return a
    return int(a) + b * 10**-(floor(log10(b))+1)
