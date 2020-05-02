alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

clist = alist + blist


for i in clist:
    if i <= 0 or i > 10:
        clist = list()
        exit()
    else:
        clist = list(set(clist))

print(sorted(clist))
