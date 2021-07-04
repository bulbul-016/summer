# Lambda function

def fun(a):
  return a * a
a = lambda x: x * x
print(a(2))

def fun(n):
  return lambda x: x * n

doubler = fun(2)
print(doubler(20))

tripler = fun(3)
print(tripler(4))