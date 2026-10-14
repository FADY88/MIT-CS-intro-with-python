# function of my creation :)
# my algorithm has O(sqrt(n)) which is polynomial
# O(n^c) c is a constant (in this case 0.5)


def divisors(n):
  """ n is an integer number
      Return a sorted list of n's divisors"""
  n = int(n)
  divisors_low = []
  divisors_high = []
  for num in range(1, int(n**0.5) + 1):
    if n % num == 0:
      divisors_low.append(num)
      if n // num != num:
        divisors_high.append(n // num)
  return divisors_low + divisors_high[::-1]

print(divisors(400000000))

# function I found on geeksforgeeks.com
# with O(n)
def Divisors(n):
  i = 1
  l = []
  while i <= n:
    if (n % i==0):
      l.append(i)
    i = i + 1
  return l
# Driver method
# print(Divisors(400000000))