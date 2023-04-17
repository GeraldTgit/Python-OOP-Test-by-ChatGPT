# ChatGPT Easy OOP Test
# Define a class called Person that has the following attributes:
#name (string) : age (integer) : gender (string)
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    # Define a method within the Person class called introduction that takes no arguments and returns a string that introduces the person by their name and age. For example, "Hi, my name is Alice and I'm 25 years old
    def introduction(self):
        return f"Hi, my name is {self.name} and I'm {self.age} years old."

# Define a class called Student that inherits from the Person class and has the following additional attributes: student_id (integer) ; major (string)
class Student(Person):
    def __init__(self, name, age, gender, student_id=0,major=""):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.major = major
    
    # Define a method within the Student class called enrollment that takes no arguments and returns a string that introduces the student by their name, age, student ID, and major. For example, "Hi, my name is Alice and I'm a 25-year-old student studying Computer Science with student ID 12345."
    def enrollment(self):
        return f"Hi, my name is {self.name} and I'm a {self.age}-year-old student studying {self.major} with student ID {self.student_id}"
        
#Create an instance of the Person class and an instance of the Student class. Call the introduction method for the Person instance and the enrollment method for the Student instance and print out the results.
Person1 = Person("Gerald",27,"Male")
Person2 = Student("Dave",28,"Male",123456,"Associate Information Technology")

print(Person1.introduction())
print(Person2.enrollment())
