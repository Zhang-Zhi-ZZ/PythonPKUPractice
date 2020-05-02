def hcf(num1, num2):
    max = 0
    if 0 < num1 < 1000 and 0 < num2 < 1000:
        for i in range(1,num1+1):
            if num1%i == 0:
                if num2%i == 0:
                    max = i

    return max


num1 = int(input(""))
num2 = int(input(""))
print(hcf(num1, num2))
