class Coordinate(object):
  def __init__(self, xval, yval):
    self.x = xval
    self.y = yval
  def distance(self, other):
    x_diff_sq = (self.x - other.x)**2
    y_diff_sq = (self.y - other.y)**2
    return (x_diff_sq + y_diff_sq)**0.5
  def to_origin(self):
    self.x = 0
    self.y = 0



# conventional or ideal way of using object of a class
c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(c.x)
print(c.distance(origin))
# equivalent way 
print(Coordinate.distance(c, origin))

class Circle(object):
  def __init__(self, center : Coordinate, radius):
    if type(center) == Coordinate and type(radius) == int:
      self.center = center
      self.radius = radius
    else:
      raise ValueError("Invalid data types")
  
  
  def is_inside(self, point : Coordinate):
    return self.radius >= point.distance(self.center)
  

  def get_radius(self):
    """ Returns the radius of self """
    return self.radius
  

  def __add__(self, c):
    """ c is a Circle object
    Returns a new Circle object whose radius is the sum of self and c's radius """
    return Circle(self.center, self.radius + c.radius)
  

  def __str__(self):
    """ A Circle's string representation is the radius """
    return str(self.radius)

point = Coordinate(3, 6)
far_point = Coordinate(4, 1)
circle = Circle(point, 4)
print(circle.is_inside(point))
print(circle.is_inside(far_point))