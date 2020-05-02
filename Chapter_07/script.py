import turtle

def tree(branchLen,t):
    t = turtle()
    if branchLen>5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen - 15, t)
        t.backward(branchLen)