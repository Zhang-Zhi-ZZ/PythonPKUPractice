alist = list(map(int, input().split()))

def foo(alist):
    blist = list()
    for i in range(1,len(alist)):
        if i % 2 != 0:
            blist.append(alist[i])
    return(blist)

print(foo(alist))