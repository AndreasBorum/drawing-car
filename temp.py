def func0(x,y):
    print(x,y)

def func1():
    return func2()

def func2():
    return 1 , 2

func0(func1)