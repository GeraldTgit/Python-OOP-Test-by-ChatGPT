"""Create a class called Car that has the following attributes and methods:
Attributes:
make (string)
model (string)
year (integer)
color (string)
Methods:
drive() that returns a string "The car is now driving."
stop() that returns a string "The car has now stopped."
get_make() that returns the make of the car.
get_model() that returns the model of the car.
get_year() that returns the year of the car.
get_color() that returns the color of the car.
Create an instance of the Car class and call each of the methods to make sure they return the expected output."""

class Car:
    def __init__(self,make,model,year=0,color=""):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
    def drive(self):
        return "The car is now driving."
        
    def stop(self):
        return "The car has now stopped."
        
    def get_make(self):
        return self.make
        
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
        
    def get_color(self):
        return self.color

car1 = Car("Hyundai","Starex 2.5 CRDi GLS AT",2021,"Black")

print(car1.drive())
print(car1.stop())
print(car1.get_make())
print(car1.get_model())
print(car1.get_year())
print(car1.get_color())
