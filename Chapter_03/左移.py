s = str(input())
n = int(input())
s1 = ''

if n<= len(s):
    s1 = s[n:]+s[0:n]
print(s1)

