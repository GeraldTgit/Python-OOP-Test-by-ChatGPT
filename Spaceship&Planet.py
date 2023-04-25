"""Define a class called Planet that has the following attributes and methods:
Attributes:
name (str): the name of the planet
radius (float): the radius of the planet in km
mass (float): the mass of the planet in kg
gravity (float): the gravity on the planet in m/s^2"""
import math
class Planet:
    def __init__(self, name: str, radius: float, mass: float, gravity: float):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.gravity = gravity
#Methods:

#get_volume() -> float: calculates and returns the volume of the planet in km^3
#get_surface_area() -> float: calculates and returns the surface area of the planet in km^2

    def get_volume(self) -> float:
        volume = "{:.2f}".format((4/3) * math.pi * self.radius ** 3)
        return volume

    def get_surface_area(self) -> float:
        surface_area = "{:.2f}".format(4 * math.pi * self.radius ** 2)
        return surface_area

earth = Planet("Earth",6371,5973600000000000000000000,9.807)

print(earth.get_volume())
print(earth.get_surface_area())

"""Define a class called Spaceship that has the following attributes and methods:
Attributes:
name (str): the name of the spaceship
speed (float): the speed of the spaceship in km/s
max_distance (float): the maximum distance the spaceship can travel in km"""
class Spaceship:
    def __init__(self, name: str, speed: float, max_distance: float):
        self.name = name
        self.speed = speed
        self.max_distance = max_distance

#Methods:
#travel(distance: float) -> float: takes a distance in km and calculates the time it would take for the spaceship to travel that distance based on its speed. Returns the time in seconds.
    def travel(self, distance: float) -> float:
        travel_time = distance / self.speed
        return travel_time
        
#land_on_planet(planet: Planet) -> str: takes a Planet object and returns a string indicating whether the spaceship can land on the planet based on its speed and the planet's gravity. If the spaceship can land, the string should say "Landing successful." Otherwise, it should say "Landing failed."
# If the speed of the spaceship is less than the gravity, the spaceship will not be able to escape the planet's gravitational pull and will crash back onto the planet.
    def land_on_planet(self, planet: Planet) -> str:
        if earth.gravity < self.speed:
            return "Landing successful."
        else:
            return "Landing failed."
        
Starship = Spaceship("USS Voyager", 5.12, 987654321)

print(Starship.travel(10123320.12))
print(Starship.land_on_planet(earth))

"""Define a subclass called Probe that inherits from the Spaceship class and has an additional attribute:
Attributes:
mission_name (str): the name of the mission the probe is on"""
class Probe(Spaceship):
    def __init__(self, name: str, speed: float, max_distance: float, mission_name:str):
        super().__init__(name, speed, max_distance)
        self.mission_name = mission_name

#Methods:
#get_info() -> str: returns a string containing the name, speed, max distance, and mission name of the probe.
    def get_info(self) -> str:
        return f"name: {self.name}, speed: {self.speed}, max distance: {self.max_distance}, mission name: {self.mission_name}"

PercyProbe = Probe("Perseverance", 0.12, 253.34, "Mars Exploration Program")
print(PercyProbe.get_info())

"""Define a subclass called Mothership that inherits from the Spaceship class and has an additional attribute:
Attributes:
fleet_size (int): the number of probe ships on board the mothership"""
class Mothership(Spaceship):
    def __init__(self, name: str, speed: float, max_distance: float, fleet_size: int):
        super().__init__(name, speed, max_distance)
        self.fleet_size = fleet_size

#Methods:
#get_info() -> str: returns a string containing the name, speed, max distance, and fleet size of the mothership.
    def get_info(self) -> str:
        return f"name: {self.name}, speed: {self.speed}, max distance: {self.max_distance}, fleet size: {self.fleet_size}"

Starfleet = Mothership("Memory Alpha", 123456789987, 987654321123, 456789123654,)
print(Starfleet.get_info())
