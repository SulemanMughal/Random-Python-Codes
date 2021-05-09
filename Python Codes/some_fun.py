def some_fun(a, b, c):
    print(a, b, c)

x = [1, 2, 3]
some_fun(*x)
#Error
#some_fun(x)


x  ={'a':2, 'b':3,'c' : 5}

some_fun(**x)
