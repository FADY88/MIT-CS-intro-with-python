(lambda x : print(x))(10)

def apply(fun, y):
  return fun(y)


print(apply(lambda z : z**2, 3))