n = int(input())
result = 0

for i in range(n+1):
    if i % 7 != 0 and '7' not in str(i):
        result += i**2

print(result)


