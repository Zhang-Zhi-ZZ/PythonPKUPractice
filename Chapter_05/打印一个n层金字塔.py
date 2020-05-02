n = int(input())
num = 1
longest = n+2
if 1 < n < 20:
    letter = '+'
    space = ' ' * (n - 1)
    for i in range(1, n+1):
        print(space + letter)
        letter += '++'
        space = space[0:-1]