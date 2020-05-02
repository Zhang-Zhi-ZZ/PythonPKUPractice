n = int(input())
N = str(n)
if len(N) == 5:
    if N[0] == N[4]:
        if N[1] == N[3]:
            print('yes')
    else:
        print('no')