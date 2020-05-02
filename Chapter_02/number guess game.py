import random

secret = random.randint(1, 100)
print('''猜数字游戏！
我想出了一个1-100的整数，你最多可以猜6次，看看能猜出来吗''')
tries = 1
while tries <= 6:
    guess = int(input("1-100的整数，第%d次猜，请输入：" % (tries,)))
    if guess == secret:
        print("Congrats! You only guessed %d times! \nThat is: %d!" %(tries, secret))
        break
    elif guess > secret:
        print("sorry, it is too large")
    else:
        print("sorry, it is too small")
    tries += 1
else:
    print("Sorry, Bye!")
