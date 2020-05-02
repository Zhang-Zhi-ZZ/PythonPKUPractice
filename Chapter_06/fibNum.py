def fbnq(number):
    n1 = 1
    n2 = 1
    for i in range(1,number-1):
        oldn1 = n1
        n1 = n2
        n2 = n2 + oldn1
    return(n2)


n = int(input(""))
print(fbnq(n))