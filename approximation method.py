guess = 0.0
a = 0.00001
epsilon = 0.01

steps = 0
num = 54321
while abs(guess**2 - num) > epsilon and guess**2 <= num:
  steps += 1
  guess += a
  # printing slows down the algorithm
  # print(guess)
print("-----")
print(guess)
print(steps)