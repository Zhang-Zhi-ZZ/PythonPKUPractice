maxnum = int(input())

for i in range(100, maxnum+1):
    num = i
    expected = i
    real = 0
    s_num = str(i)
    n = len(s_num)
    for j in s_num:
        real += int(j)**n
    if real == expected:
        print(expected)


