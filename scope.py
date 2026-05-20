x = 10
def outerfun():
    global x
    x = 11
    y = 20
    def innerfun():
        nonlocal y
        y = 22
        print(y)
    innerfun()
    print(y)
outerfun()
print(x)