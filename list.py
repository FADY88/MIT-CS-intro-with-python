s = [1, 3, 4]
print(s)
s[0] = 5
print(s)

def make_ordered_list(n):
  """ n is a positive int
  returns a list containing all ints
  in order from 0 to n (inclusive)"""
  l = []
  for i in range(n + 1):
    l.append(i)
  return l

def remove_elem(l, e):
  """l is a list
  returns a list with elements in the same order as l but 
  without any elements equal to e"""
  s = []
  for i in l:
    if i != e:
      s.append(i)
  return s


print(make_ordered_list(5))
print(remove_elem([1, 2, 2, 2], 2))


name = "fady adel"
li = list(name)
print(li)
name = name.split()
# print(name)
# anything in the quotes will be added between every two elements
name = ' '.join(name)
print(name)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# enumerate allows you to iterate over indices and elements at once
def square_list(nums):
  for i, e in enumerate(nums):
    nums[i] = e**2


square_list(numbers)
print(numbers)
# id function returns the memory address of an object
print(hex(id(name)))
print(id(s))

# mutating lists is tricky be careful with them