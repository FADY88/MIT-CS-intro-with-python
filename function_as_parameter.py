def apply(criteria, n):
  count = 0
  for i in range(n + 1):
    if criteria(i):
      count += 1
  return count


def is_even(n):
  return n % 2 == 0


def is_prime(n):
  if n < 2:
    return False
  elif n == 2:
    return True
  for i in range(2, n):
    if n % i == 0:
      return False
  return True


how_many_even = apply(is_even, 10)
print(how_many_even)
how_many_prime = apply(is_prime, 7)
print(how_many_prime)


# functions can return function object
def make_prod(a):
  def g(b):
    return a*b
  return g

var = make_prod(2)(3)
print(var)