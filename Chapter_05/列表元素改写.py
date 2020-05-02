alist = list(map(int, input().split()))
blist = list()
for i in alist:
    if i%2==1:
        i = i**2
        blist.append(i)
    else:
        i = int(i/2)
        blist.append(i)

print(sorted(blist))