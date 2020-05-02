n = int(input())

for i in range(1, n):
    nums = 0
    for j in range(1, i):
        if i%j == 0:
            nums+=j
    if nums == i:
        print(i)
