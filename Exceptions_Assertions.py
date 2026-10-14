try:
  x = int(input("Enter a number: "))
  y = int(input("Enter a number: "))
  print(x/y)
except ValueError:
  print("Could not convert to a number.")
except ZeroDivisionError:
  print("Can't divide by zero.")
except:
  print("Something went very wrong.")
  # you can raise your own errors(stops the execution)
  raise ValueError("Something went wrong.")

# there are also else: and finally:

def x(lnum, ldenom):
  l = []
  for i in range(len(lnum)):
    try:
      l.append(lnum[i] / ldenom[i])
    except:
      raise ValueError("can't divide by zero")
  return l
print(x([4, 5, 6], [1, 2, 3]))
# print(x([4, 5, 6], [1, 0, 3]))

# Assertions 
# assert <condition>, error message
def divide(x, y):
  assert y != 0, "Can't divide by zero"
  return x / y

print(divide(5, 3))
print(divide(5, 0))