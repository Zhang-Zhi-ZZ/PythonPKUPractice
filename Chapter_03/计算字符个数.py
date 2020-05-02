s = str(input())
s1 = str(s.lower().split()[0])
c = str(s.lower().split()[-1])

if len(s1) == 0:
    exit()
if len(c) == 0:
    exit()
if len(c) >= 1:
    print(s1.count(c))

