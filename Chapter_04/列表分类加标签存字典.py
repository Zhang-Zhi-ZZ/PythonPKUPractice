alist = list(map(int, input().split()))

for i in alist:
    if i < 0 and len(alist) % 2 != 0:
        exit()

mid = len(alist)/2
dic = {}
dic['1'] = alist[0:int(mid)]
dic['2'] = alist[int(mid): ]

print(dic)


