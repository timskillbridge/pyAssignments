from __future__ import annotations
import subprocess

class CarManager:
    all_cars = []
    total_cars = 0
    id = 0

    @classmethod
    def __repr__(cls):
        return (f"There are {cls.total_cars} cars in the shop\n {cls.all_cars}")

    @classmethod
    def delay(cls):
        input("Press any key to continue")
        CarManager.clearScreen()

    @classmethod
    def displayCars(cls):
        if len(CarManager.all_cars) > 0:
            print("These are the cars in your inventory:\n")
            cls.delay()
            pass
        for x,y in enumerate(CarManager.all_cars):
            # tMileage = int(y.mileage)
            print(f"ID# {y.id}: {y.year} {y.model} {y.make} with {int(y.mileage):,} miles. {f'It could use some work: {y.services}' if len(y.services) > 0 else ''}")
        # CarManager.delay()


    @classmethod
    def getMenuInput(cls):
        userInput = input()
        
        try:
            userInput = int(userInput)
        except:
            return False
            pass
        return userInput

    @classmethod
    def clearScreen(cls):
        subprocess.run('clear',shell=True)

    @classmethod
    def validateInput(cls,arglist, type):
        if type == int:
            try:
                for x,y in enumerate(arglist):
                    y = int(y)
            except:
                return False
            return arglist
        elif type == str:
            try:
                for x,y in enumerate(arglist):
                    y = str(y)
            except:
                return False
            return arglist


    @classmethod
    def add_vehicle(cls):
            make = input("make: ")
            model = input("model: ")
            year = input("year: ")
            mileage = input("mileage ")
            if CarManager.validateInput([make,model],str) and CarManager.validateInput([year,mileage],int):
                new_vehicle_dictionary = {
                    "make" : make,
                    "model" : model,
                    "year" : year,
                    "mileage" : mileage
                }
                # CarManager.id +=1
                CarManager.all_cars.append(CarManager(**new_vehicle_dictionary))

                print(f'''
                      Added your: {year} {make} {model}
                      Reference ID: {len(CarManager.all_cars)}''')
                CarManager.total_cars +=1
                CarManager.delay()
            else:
                print("\nThe data entered was not valid, try again\n")
                CarManager.delay()
                return False
            
    @classmethod
    def serviceCar(cls):
        CarManager.clearScreen()
        if len(CarManager.all_cars) == 0:
            print("\nThere are no cars to service")
        
            CarManager.delay()
            pass
        else:
            CarManager.displayCars()
            print(f'''\n1
              Select a car to service by entering its ID#: \n
''')
            menuitem = cls.getMenuInput()-1
            if not cls.validateInput([menuitem],int):
                pass

            if -1 < menuitem < len(CarManager.all_cars):
                service_rendered = input("what was the service?\n")
                if not cls.validateInput([service_rendered],str):
                    pass
                # print(f"{service_rendered} and car # {menuitem} and\n {len(cls.all_cars)}")
                cls.service_setter(menuitem,service_rendered)
                cls.clearScreen()
                pass

    
    # @service.setter
    @classmethod
    def service_setter(cls,carID,serviceItem):
        cls.all_cars[carID].services.append(serviceItem)
            

    
    def __rpr__(self):
        items = []
        for x in enumerate(self.all_cars):
            items.append(f"{x.year} {x.make} {x.model}\n")
        
        return f'''
        Cars in Inventory:
        {"".join(items)}
        # of Cars in Inventory: {self.total_cars}'''
    
# <---- essentially the car class:
    def __init__(self,make,model,year,mileage):
        self.id = self.id + 1
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.services = []
        CarManager.id +=1

#----------------Main program--------------------------------
ca1 = CarManager
print(ca1)
running = True
while running:
    CarManager.clearScreen()
    print(f'''
            1. Add a car
            2. View all cars
            3. View total number of cars
            4. Service a car
            5. Update mileage
            7 Quit
            ''')
    whereto = CarManager.getMenuInput()
    match whereto:
        case 7:
            CarManager.clearScreen()
            running = False
        case 1:
            CarManager.clearScreen()
            print(f'''
                    
                    What kind of car are you adding?
                  
                    ''')
            CarManager.add_vehicle()
            CarManager.clearScreen()
            pass
        case 2:
            CarManager.clearScreen()
            
            if len(CarManager.all_cars) > 0:
                
                CarManager.displayCars()
                CarManager.delay()
                CarManager.clearScreen()
                pass
            else:
                print("There are no cars in your inventory, try adding some\n")
                CarManager.delay = input("Press any key to continue")
            CarManager.clearScreen()
            pass
        case 3:
            CarManager.clearScreen()
            if len(CarManager.all_cars) >0:
                if len(CarManager.all_cars) == 1:
                    print(f'''
                      There is only {len(CarManager.all_cars)} car in the inventory
                      ''')
                else:
                    print(f'''
                      There are {len(CarManager.all_cars)} cars in the inventory
                      ''')
                CarManager.delay()
            else:
                print("There aren't any vehicles in the inventory")
                CarManager.delay()
                pass
        case 4:
            CarManager.serviceCar()
            pass


            
        


# ca1 = CarManager("Ford","Escort",1997,105891)
