import subprocess
import csv


class Animal:
    def __init__(self, name, age, species):
        if not set(map(lambda x: isinstance(x,str), [name, species])) == {True} \
            or isinstance(age,int) != int \
            or ["DOG","CAT"].index(species.upper()) != -1:
            print(f"The animal you've attempted to add had one or more invalid properties")
        


def clearScreen():
    subprocess.run('clear', shell=True)    

running = True
while running:
    clearScreen()
    print(f"RUNNING")
    print(f'''
          Dogs and Cats, living together...mass hysteria!
          1. View Animals by type
          2. Enter new animal
          3. Quit
          ''')
    try:
        goto = int(input(" What would you like to do? : \n"))
    
        if isinstance(goto,int) == True and 0 < goto < 4:
            match goto:
                case 1:
                    clearScreen()
                    print(f'''
                        Cats or Dogs?
                        1. Dogs
                        2. Cats
                        ''')
                    try:
                        animalType = int(input("Would you like to see cats or dogs? "))

                        if isinstance(animalType,int) != True or 0 > animalType >4:
                            print("Not a valid entry, press any key to go back to the menu")
                            animalType = input('')
                            clearScreen()
                            pass
                        else:
                            match animalType:
                                case 1:
                                    clearScreen()
                                    with open('data/dogs.csv', newline = '') as infile:
                                        pets = csv.reader(infile, delimiter=',', quotechar='|')
                                        next (pets)
                                        for row in pets:
                                            info = [x for x in row]
                                            print(f'{row[0]} is a {row[1]} year old {row[2]}')
                                        wait = input('\nPress any key to return')
                                        clearScreen()
                                case 2:
                                    clearScreen()
                                    with open('data/cats.csv', newline = '') as infile:
                                        pets = csv.reader(infile, delimiter=',', quotechar='|')
                                        next (pets)
                                        for row in pets:
                                            info = [x for x in row]
                                            print(f'{row[0]} is a {row[1]} year old {row[2]}')
                                        wait = input('\nPress any key to return')
                                        clearScreen()
                    except:
                        pass

                case 2:
                    clearScreen()
                    print(f'''
                        Add cats or dog?
                        1. Dogs
                        2. Cats
                        ''')
                    try:
                        animalType = int(input("Would you like to add, cats or dogs? "))

                        if isinstance(animalType,int) != True or 0 > animalType >4:
                            print("Not a valid entry, press any key to go back to the menu")
                            animalType = input('')
                            clearScreen()
                            pass
                        else:
                            try:
                                pName = input("Pet Name ")
                                pAge = int(input("Pet Age "))
                                pSpecies = input("Species ")
                            except:
                                transition = input("Not valid pet parameters, hit any key to return to the menu")
                                pass
                          
                            if animalType == 1:
                                filepath = "data/dogs.csv"
                            else:
                                filepath = "data/cats.csv"

                            with open(filepath, "a", newline = '\n') as infile:
                                pets = csv.writer(infile)
                                pets.writerow([pName,pAge,pSpecies])
                                
                            transition = input(f'Added {pName}, press any key')
                    except:
                        pass

                case 3:
                    clearScreen()
                    running = False
                    pass
    except:
        pass