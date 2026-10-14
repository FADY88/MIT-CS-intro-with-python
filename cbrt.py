epsilon = 0.01

steps = 0
num = 27
if num < 1:
  upper_bound = 1
else:
  upper_bound = num
lower_bound = 0
guess = (upper_bound + lower_bound) / 2

while abs(guess**3 - num) >= epsilon:
  if guess**3 > num:
    upper_bound = guess
  else:
    lower_bound = guess
  
  guess = (upper_bound + lower_bound) / 2
  # printing slows down the algorithm
  steps += 1
  print(guess)



print("-----")
print(guess)
print(steps)