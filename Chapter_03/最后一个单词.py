s = str(input())

if len(s)<5000:
    n = len(s)
    length = len(s.split()[-1:][0])
    print(length)