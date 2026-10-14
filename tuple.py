t = (3, 5, 4, "fady")
# print(max(t)) # error: max support one type sequence

# swap variables using tuples
a = 5
b = 7
# evaluate the left side then map it to the right side
(b, a) = (a, b)
print(a, b)


# return a tuple from a function
def quotient_remainder(x, y):
  q = x // y
  r = x % y
  return (q, r)

both = quotient_remainder(12, 4)
(quot, rem) = quotient_remainder(12, 4)


# function takes variable number of parameters
# by putting them in a tuple(* notation)
def mean(*args):
  total = 0
  for a in args:
    total += a
  return total/len(args)

print(mean(1, 2, 3, 4, 5))
