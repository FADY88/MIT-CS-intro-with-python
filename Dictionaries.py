def find_grades(grades, students):
  """ grades is a dict mapping student names (str) to grades (str)
      students is a list of student names
  returns a list containing the grades for students (in same order)"""
  l = []
  for student in students:
    l.append(grades[student])
  return l


d = {'Ana' : 'B', 'Matt' : 'C', 'John' : 'B', 'Katy' : 'A'}
print(find_grades(d, ['Matt', 'Katy']))

# delete entry from a dictionary use del()
del(d['Matt'])

# in keyword checks for keys
print('Matt' in d) # False

def find_in_L(Ld, k):
  """ Ld is a list of dicts
      k is an int
  returns True if k is a key in any dicts of Ld and False otherwise"""
  for d in Ld:
    if k in d:
      return True
  return False

d1 = {1 : 2, 3 : 4, 5 : 6}
d2 = {2 : 4, 4 : 6}
d3 = {1 : 1, 3 : 9, 4 : 16, 5 : 25}
print(find_in_L([d1, d2, d3], 2)) # True
print(find_in_L([d1, d2, d3], 25)) # False

# to iterate over each key in a dict 
d1.keys() # returns dict_key([1, 2, 5]) as dict_key
list(d1.keys()) # returns [1, 2, 5] as list
# can use values() function to get values in a dict
# item function gives the keys and the values

def count_matches(d):
  """ d is a dict
  returns how many entries in d have the key equal to its value"""
  count = 0
  for k, v in d.items():
    if k == v:
      count += 1
  return count


d = {1:2, 3:4, 5:6}
print(count_matches(d))
d = {1:2, 'A':'A', 5:5}
print(count_matches(d))