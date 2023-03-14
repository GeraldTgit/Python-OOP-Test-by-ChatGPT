#Define a class named Square that inherits from the Rectangle class and has the following additional attributes and methods:
#Attributes: side_length (float)
#Method: area() that calculates and returns the area of the square.

class Square(Rectangle):
  def __init__(self, side_length=0):
    super().__init__(side_length, side_length)
    self.side_length = side_length
    
  def area(self):
    return self.side_length ** 2
    
S1 = Square(3)

print(S1.area())
