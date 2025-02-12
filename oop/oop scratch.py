"""
Mechanic Shop:
- Owner
  - Name
  - Contact Information
- Automobiles
  - tires
  - color
  - miles
  - engine
- Bikes
  - tires
  - color
  - engine
"""


class Owner:

    def __init__(self, name, phone, sign=None):
        self.name = name
        self.phone = phone
        self.sign = sign


"""
Create an instance of a class utilizing
dictionaries within python with kwargs **
"""
rod = {"phone": "555-555-5555", "name": "Rod"}
adam = {"name": "Adam", "phone": "555-555-5555"}
rod_class = Owner(phone="555-555-5555", name="Rod")
rod_class = Owner(**rod)
adam_class = Owner(**adam)

"""
Creating Automobiles
"""


class Automobile:
    # class attribute
    vehicles = {}

    def __init__(self, tires, color, miles, engine, owner = None):
        self.tires = tires
        self.color = color
        self.miles = miles
        self.engine = engine
        self.owner = owner
        self.running = False

    def __repr__(self):
        return f"Automobile color {self.color} with {self.tires} belongs to {self.owner.name if self.owner else None}"

    def start_ignition(self):
        if not self.running:
            self.running = not self.running
        return f"This vehicle has now been turned on"

    def turn_vehicle_off(self):
        if self.running:
            self.running = not self.running
        return f"This vehicle has now been turned off"
    
    """
    Need to make accessible to the class itself since the goal
    of this method is to change a class level attribute
    """
    @classmethod
    def add_a_vehicle(cls):
        new_vic_dic = {
            "tires" : input("How many tires in this car?\n"),
            "color" : input("What color is this car?]\n"),
            "miles" : input("How many miles are in this car?\n"),
            "engine" : input("Engine size: \n"),
        }
        cls.vehicles[max(cls.vehicles.keys())+1] = cls(**new_vic_dic) # cls == Automobile
        return "A new vehicle has been added to the shop!"
    
    """
    Static methods do not interact nor change the values of class attributes
    or instance attributes they are behaviors living outside the class itself
    """
    @staticmethod
    def announce_opening():
        return f"THE SHOP IS NOW OPEN"


corola = {"tires": 4, "color": "gray", "miles": 1000, "engine": 4, "owner": adam_class}
truck = {"tires": 4, "color": "black", "miles": 2000, "engine": 4, "owner": rod_class}

corola_class = Automobile(**corola)
truck_class = Automobile(**truck)
# Automobile.vehicles[1] = corola_class
# Automobile.vehicles[2] = truck_class
# print(truck_class.vehicles)
# print(corola_class.vehicles)
# print(Automobile.vehicles)
# print(Automobile.vehicles[1].tires)
"""
running instance methods from a class
"""
# Automobile.start_ignition()
# raises error due to not having access to the instance

"""
Instance level methods
"""
# print(corola_class.start_ignition())
# print(corola_class.running)
# print(corola_class.turn_vehicle_off())
# print(corola_class.running)
"""
Class level methods
"""
# Automobile.add_a_vehicle()
# print(Automobile.vehicles)

"""
Static methods
"""

print(Automobile.vehicles)
print(corola_class.vehicles)
print(truck_class.vehicles)
print(truck_class)