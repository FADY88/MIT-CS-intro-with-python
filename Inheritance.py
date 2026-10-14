class Animal(object):
  def __init__(self, age):
    self.age = age
    self.name = None
  
  def __str__(self):
    return "animal:"+str(self.name)+":"+str(self.age)
  
  def get_age(self):
    return self.age
  
  def get_name(self):
    return self.name
  
  def set_age(self, age):
    self.age = age

  def set_name(self, name = ""):
    self.name = name

def make_animals(l1, l2):
  result = []
  for i in range(len(l1)):
    result.append(Animal(l1[i]))
    result[i].set_name(l2[i])
  return result

l1 = [2, 5, 1]
l2 = ["blobfish", "crazyant", "parafox"]
animals = make_animals(l1, l2)
for i in animals:
  print(i)

print()

class Cat(Animal): # inherit from Animal class
  def speak(self):
    print("meow")
  def __str__(self): # override print()
    return "cat:"+str(self.name)+":"+str(self.age)
  
class Person(Animal):
  def __init__(self, name, age):
    Animal.__init__(self, age)
    self.set_name(name)
    self.friends = []
  def get_friends(self):
    return self.friends.copy()
  def add_friend(self, fname):
    if fname not in self.friends:
      self.friends.append(fname)
  def speak(self):
    print("hello")
  def age_diff(self, other):
    print(abs(self.age - other.age), "year difference")
  def __str__(self):
    return "Person:"+str(self.name)+":"+str(self.age)
  

def make_pets(d):
  for p, c in d.items():
    print(p.get_name()+":"+c.get_name())


p1 = Person("ana", 86)
p2 = Person("james", 7)
c1 = Cat(1)
c1.set_name("furball")
c2 = Cat(1)
c2.set_name("fluffsphere")

d = {p1:c1, p2:c2}
make_pets(d)

print()


class Student(Person):
  def __init__(self, name, age, major=None):
    Person.__inti__(self, name, age)
    self.major = major
  def change_major(self, major):
    self.major = major
  def __str__(self):
    return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
  
class Rabbit(Animal):
  tag = 1
  def __init__(self, age, parent1=None, parent2=None):
    Animal.__init__(self, age)
    self.parent1 = parent1
    self.parent2 = parent2
    # shared attribute across all instance of the same class
    self.rid = Rabbit.tag
    Rabbit.tag += 1

  def get_parent1(self):
    return self.parent1

  def get_parent2(self):
    return self.parent2
  
  def __add__(self, other):
    return Rabbit(0, self, other)
  
  def __eq__(self, other):
    parents_same = (self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid)
    parents_opp = (self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid)
    return parents_opp or parents_same