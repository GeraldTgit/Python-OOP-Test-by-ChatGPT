"""Define a class called Spacecraft that has the following attributes and methods:
Attributes:
name (str): the name of the spacecraft
speed (float): the speed of the spacecraft in km/s
max_distance (float): the maximum distance the spacecraft can travel in km"""
class Spacecraft:
    def __init__(self, name: str, speed: float, max_distance: float):
        self.name = name
        self.speed = speed
        self.max_distance = max_distance

#Methods:
#travel(distance: float) -> float: takes a distance in km and calculates the time it would take for the spacecraft to travel that distance based on its speed. Returns the time in seconds.
    def travel(self, distance: float) -> float:
        travel_time = (distance / self.speed) * 60
        return travel_time

"""Define a subclass called Spaceship that inherits from the Spacecraft class and has an additional attribute:
Attributes:
crew_size (int): the number of crew members on board the spaceship"""
class Spaceship(Spacecraft):
    def __init__(self, name: str, speed: float, max_distance: float, crew_size: int):
        super().__init__(name, speed, max_distance)
        self.crew_size = crew_size

#Methods:
#get_info() -> str: returns a string containing the name, speed, max distance, and crew size of the spaceship.
    def get_info(self) -> str:
        return f"name: {self.name}, speed: {self.speed}, max distance: {self.max_distance}, crew size: {self.crew_size}"

"""Define another subclass called Probe that inherits from the Spacecraft class and has an additional attribute:
Attributes:
mission_name (str): the name of the mission the probe is on"""
class Probe(Spacecraft):
    def __init__(self, name: str, speed: float, max_distance: float, mission_name: str):
        super().__init__(name, speed, max_distance)
        self.mission_name = mission_name
#Methods:
#get_info() -> str: returns a string containing the name, speed, max distance, and mission name of the probe.
    def get_info(self) -> str:
        return f"name: {self.name}, speed: {self.speed}, max distance: {self.max_distance}, mission name: {self.mission_name}"

#Create an instance of Spaceship and an instance of Probe. Test all of the methods on each instance to make sure they return the expected output."""

Spacetravel1 = Spacecraft("Starship", 10000, 9999999)
Spacetravel2 = Spaceship("USS Enterprise", 100000, 99999999,3126)
Spacetravel3 = Probe("USS Discovery", 19878654, 99999999,"Spore Drive Testing")

print(Spacetravel1.travel(5123.12))
print(Spacetravel2.get_info())
print(Spacetravel3.get_info())
