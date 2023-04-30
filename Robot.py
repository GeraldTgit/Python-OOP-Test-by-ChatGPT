"""Sure, here's a quiz related to robotics:

Define a class called Robot that has the following attributes and methods:

Attributes:
- name (str): the name of the robot
- height (float): the height of the robot in meters
- weight (float): the weight of the robot in kilograms
- battery_life (float): the battery life of the robot in hours
- max_speed (float): the maximum speed of the robot in m/s

Methods:
- move(distance: float) -> float: takes a distance in meters and calculates the time it would take for the robot to travel that distance based on its max speed. Returns the time in seconds.
- charge(battery_time: float) -> None: takes a time in hours and adds it to the robot's battery life.
- speak(message: str) -> str: takes a message and returns a string containing the robot's name and the message.
- __str__() -> str: returns a string representation of the robot in the following format: "Name: [name], Height: [height] m, Weight: [weight] kg, Battery Life: [battery_life] hrs, Max Speed: [max_speed] m/s"""

class Robot:
    def __init__(self, name: str, height: float, weigth: float, battery_life: float, max_speed: float):
        self.name = name
        self.height = height
        self.weigth = weigth
        self.battery_life = battery_life
        self.max_speed = max_speed

    def move(self, distance: float) -> float:
        return distance / self.max_speed
         
    def charge(self, battery_time: float) -> None:
        self.battery_life += battery_time

    def speak(self, message: str) -> str:
        return f"{self.name}: {message}"

    def __str__(self) -> str:
        return f"Name: {self.name}, Height: {self.height} m, Weight: {self.weigth} kg, Battery Life: {self.battery_life} hrs, Max Speed: {self.max_speed} m/s"

robot_1 = Robot("Atlas", 1.5, 89, 3, 2.5)

print(robot_1.move(10))
print(robot_1.charge(.9))
print(robot_1.speak("Hello there!"))
print(robot_1)

"""Define a subclass called IndustrialRobot that inherits from the Robot class and has an additional attribute:

Attributes:
- arm_length (float): the length of the robot's arm in meters

Methods:
- pick_and_place(weight: float, distance: float) -> float: takes a weight in kilograms and a distance in meters and calculates the time it would take for the robot to pick up the object, move it the specified distance, and place it down. The time should be calculated based on the robot's max speed and the weight of the object (heavier objects will take longer to pick up and move). Returns the total time in seconds.
- __str__() -> str: returns a string representation of the industrial robot in the following format: "Name: [name], Height: [height] m, Weight: [weight] kg, Battery Life: [battery_life] hrs, Max Speed: [max_speed] m/s, Arm Length: [arm_length] m"""

class IndustrialRobot(Robot):
    def __init__(self, name: str, height: float, weigth: float, battery_life: float, max_speed: float, arm_length: float):
        super().__init__(name, height, weigth, battery_life, max_speed)
        self.arm_length = arm_length

    def pick_and_place(self, weight: float, distance: float) -> float:
        deceleration = weight / self.max_speed
        return distance / self.max_speed - deceleration

    def __str__(self) -> str:
        return f"Name: {self.name}, Height: {self.height} m, Weight: {self.weigth} kg, Battery Life: {self.battery_life} hrs, Max Speed: {self.max_speed} m/s, Arm Length: {self.arm_length} m"

robot_2 = IndustrialRobot("Spot", .7, 31.7, 3, 1.6, .98)
print(robot_2.pick_and_place(2, 10))
print(robot_2)

"""Define a subclass called HumanoidRobot that inherits from the Robot class and has additional attributes and methods:

Attributes:
- num_legs (int): the number of legs the robot has
- num_arms (int): the number of arms the robot has

Methods:
- walk(distance: float) -> float: takes a distance in meters and calculates the time it would take for the robot to walk that distance based on its max speed. Returns the time in seconds.
- wave() -> str: returns a string containing the robot's name and "waves hello!"""

"""The HumanoidRobot subclass should also override the __str__() method to return a string representation of the humanoid robot in the following format: "Name: [name], Height: [height] m, Weight: [weight] kg, Battery Life: [battery_life] hrs, Max Speed: [max_speed] m/s, Legs: [num_legs], Arms: [num_arms]"""

class HumanoidRobot(Robot):
    def __init__(self, name: str, height: float, weigth: float, battery_life: float, max_speed: float, num_legs: int, num_arms: int):
        super().__init__(name, height, weigth, battery_life, max_speed)
        self.num_legs = num_legs
        self.num_arms = num_arms

    def walk(self, distance: float) -> float:
        return distance / self.max_speed

    def wave(self) -> str:
        return f"{self.name}: waves hello!"

    def __str__(self) -> str:
        return f"Name: {self.name}, Height: {self.height} m, Weight: {self.weigth} kg, Battery Life: {self.battery_life} hrs, Max Speed: {self.max_speed} m/s, , Legs: {self.num_legs}, Arms: {self.num_arms}"

Optimus = HumanoidRobot("Tesla Bot", 1.73, 57, 8, 2.2, 2, 2)
print(Optimus.walk(10))
print(Optimus.wave())
print(Optimus)
