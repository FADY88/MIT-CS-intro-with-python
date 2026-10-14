epsilon = 10e-10

steps = 0
num = 0.5
if num < 1:
  upper_bound = 1
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
  # printing slows down the algorithm
  steps += 1
  print(guess)



print("-----")
print(guess)
print(steps)