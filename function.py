def sqrt(num):
  epsilon = 0.01
  steps = 0
  if num < 1:
    upper_bound = 1
  elif num < 0:
    return 0
  else:
    upper_bound = num
  lower_bound = 0
  guess = (upper_bound + lower_bound) / 2
  while abs(guess**2 - num) >= epsilon:
    if guess**2 > num:
      upper_bound = guess
    else:
      lower_bound = guess
    guess = (upper_bound + lower_bound) / 2
    steps += 1
  return guess

# A hard function I'm prude that I made it way more efficient then what the doctor did in lecture
def count_nums_with_sqrt_close_to(n, epsilon):
  """n is an int > 2
    epsilon is a positive number < 1
    returns how many integers have a square within epsilon of n"""
  if n - epsilon < 0:
    low = 0
  else:
    low = int((n - epsilon)**2)
  high = int((n + epsilon)**2)
  count = 0
  for i in range(low, high + 1):
    square = sqrt(i)
    if abs(square - n) <= epsilon:
      print("sqrt of", i, "is", square)
      count += 1
  return count


print(count_nums_with_sqrt_close_to(10, 1))

