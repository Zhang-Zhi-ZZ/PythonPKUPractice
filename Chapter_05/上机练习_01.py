#给定n， 计算1+2！+3！+... + n! 的值

n = int(input())
num = 1
sum = 0
for i in range(1,n+1):
    num = i*(num)
    sum += num


print(sum)