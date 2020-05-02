def bubbleSort(alist):
    for i in range(len(alist)):
        for l in range(0,len(alist)-1):
            r = l+1
            if alist[r] < alist[l]:
                alist[l], alist[r] = alist[r], alist[l]
    return alist


alist = list(map(int, input().split()))
print(bubbleSort(alist))
