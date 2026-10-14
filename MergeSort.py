def merge_sort(l):
  # base case
  if len(l) == 1:
    return l
  # sort left half and right half
  l1 = merge_sort(l[len(l)//2:]) 
  l2 = merge_sort(l[:len(l)//2])
  # merge
  return merge(l1, l2)


def merge(left, right):
  result = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  for r in left[i::]:
    result.append(r)
  for r in right[j::]:
    result.append(r)
  return result

left = [1, 4, 6, 8]
right = [0, 2, 5, 9]
li = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(merge(left, right))
print(merge_sort(li))