theNum = int(input())
theResult = list()

for i in range(2,theNum):
    for j in range(2,i):
        if i % j == 0:
            j = 0
            break
    else:
        theResult.append(i)

print(theResult)

