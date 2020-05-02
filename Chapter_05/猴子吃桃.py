nDay = int(input())

if 1 < nDay < 11:
    P = 1
    for i in range(1, nDay):
        P = (P+1)*2

    print(P)