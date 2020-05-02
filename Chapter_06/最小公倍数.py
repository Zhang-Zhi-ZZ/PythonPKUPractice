def lcm(n1, n2):
    min = n1 * n2
    for i in range(n1*n2, 1, -1):
        if i % n1 == 0:
            if i % n2 == 0:
                min = i
    return min


num1=int(input(""))
num2=int(input(""))
print(lcm(num1, num2))
