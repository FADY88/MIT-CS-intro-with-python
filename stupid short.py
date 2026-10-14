# a short video I watched on youtube that had this problem
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list)

def even_odd(list):
  not_done = True
  while not_done:
    not_done = False
    for i in range(len(list) - 2):
      if list[i] % 2 == 1 and list[i + 1] % 2 == 0:
        (list[i], list[i + 1]) = (list[i + 1], list[i])
        not_done = True
  return list

print(even_odd(list))