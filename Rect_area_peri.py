#Define a class named Rectangle that has the following attributes and methods:
#Attributes: width (float), height (float)
#Methods: area() that calculates and returns the area of the rectangle, perimeter() that calculates and returns the perimeter of the rectangle.

class Rectangle:
  def __init__(self, width=0,height=0):
    self.width = float(width)
    self.height = float(height)
  
  def area(self):
    return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)
        
R1 = Rectangle(3.3, 36.1)

print(R1.area())
print(R1.perimeter())