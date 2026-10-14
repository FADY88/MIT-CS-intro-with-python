class Fraction(object):
  def __init__(self, n, d):
    if d == 0:
      raise ValueError("Denominator can't be zero")
    self.num = n
    self.denom = d


  def __mul__(self, oth):
    top = self.num * oth.num
    bottom = self.denom * oth.denom
    return Fraction(top, bottom)
  

  def __add__(self, oth):
    top = self.num * oth.denom + self.denom * oth.num
    bottom = self.denom * oth.denom
    return Fraction(top, bottom)
  

  def get_inverse(self):
    """ Returns a float representing 1/self """
    return self.denom / self.num
  

  def invert(self):
    """ Sets self's num to denom and vice versa
        returns None"""
    self.num, self.denom = self.denom, self.num


  def __str__(self):
    if self.denom == 1:
      return str(self.num)
    return str(self.num) + "/" + str(self.denom)
  

  def __float__(self):
    return self.num / self.denom
  

  def reduce(self):
    def GCD(n, d):
      while d != 0:
        d, n = n%d, d
      return n
    if self.denom == 0:
      return None
    elif self.denom == 1:
      return Fraction(self.num, 1)
    else:
      gcd = GCD(self.num, self.denom)
      top = int(self.num / gcd)
      bottom = int(self.denom / gcd)
    return Fraction(top, bottom)


f1 = Fraction(1, 4)
print(f1.get_inverse())
print(f1)
print(f1.invert())
print(f1.get_inverse())
print(f1)
f1.invert()

f1 = Fraction(8, 16)

print(f1.reduce())