import math

a = int(input())
b = int(input())

if a > 0 and b > 0:
    c = math.sqrt(a**2 + b**2)
    h = (a*b)/c
    print(round(h, 2))

