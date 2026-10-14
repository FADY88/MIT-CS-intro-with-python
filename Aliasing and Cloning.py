import copy

def remove_all(l, e):
  """L is a list
  Mutates L to remove all elements in L that are equal to e
  Returns None"""
  # copy list to another
  LCopy = l[:] # list(L)
  l.clear()
  for i in LCopy:
    if i != e:
      l.append(i)

L = [1, 2, 2, 2]
remove_all(L, 2)
print(L)

# making alias for the same list
L_alias = L
LCopy = L_alias.copy()
# deep copy if list has mutable objects
LDeepCopy = copy.deepcopy(L_alias)

################################
# common pattern
def f(L):
  Lnew = []
  for e in L:
    if e%2 == 0:
      Lnew.append(e**2)
  return Lnew
# shortcut using list comprehensions
Lnew = [e**2 for e in L if e%2 == 0]
# can apply to to range or string (iterable)
sequence = [n * 2 for n in range(6) if n > 2] # [6, 8, 10]
print(sequence)