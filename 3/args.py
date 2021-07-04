def f(a,b, *args):
    print(a,b, args)
f(2, 3, "k", 5, 6)

def f1(a,b, *args):
    print(a,b)
    for arg in args:
        print(arg)
f1('baby', 'detka', 16, 12, 2002)

def f3(**kwargs): # **kwargs - optional keyword arguments ---> dict
  print(kwargs)
f3(name='Bob', age=20, gpa=3.0)


def f4(a, b=2, *arg, **kwargs): # default value
  print(a + b)
f4(2, 4)