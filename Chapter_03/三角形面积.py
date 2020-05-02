import math

a = int(input())
b = int(input())
c = int(input())

if a<1000 and b<1000 and c<1000:
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('%.2f'%S)
