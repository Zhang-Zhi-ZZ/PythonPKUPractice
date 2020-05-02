a1 = int(input())
a2 = int(input())
n = int(input())

d = a2 - a1

if n >= 2:
    result = a1 + d*(n-1)
    print(result)