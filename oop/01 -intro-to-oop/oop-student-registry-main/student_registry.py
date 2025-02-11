import re
class Student:
    def __init__(self, name, age=13, grade="12th"):
        if not set(map(lambda x: isinstance(x,str), [name,grade])) == {True} or not isinstance(age,int) == True or \
        not isinstance(name,str) == True and \
        len(name) >=3 and \
        name[0] == name[0].upper() and \
        (" " not in name or len(re.findall(r"\W",name)) != 0):
            print("invalid variables passes")
            return
        self.__name = name
        self.__age = age
        self.__grade = grade
    
    def __str__(self):
        return f"{self.__name} is a {self.__age} year old in {self.__grade} grade"
    
    @property
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def name(self,name):
        
        # print(specialC)
        if  isinstance(name,str) != True or \
            len(name) <3 or \
            name[0] != name[0].upper() or \
            len(re.findall(r"\W",name)) != 0:
            print(f"{name} is not a valid name")
            return self.__name
        
        self.__name = name

    
    @property
    def get_age(self):
        return self.__age
    @get_age.setter
    def age(self,age):
        if not isinstance(age,int) == True or age >110:
            print(f"{age} is not a valid age")
            return self.__age
        self.__age = age
    
    @property
    def get_grade(self):
        return f"{self.__grade}"
    @get_grade.setter
    def grade(self,grade):
        if isinstance(grade,str) != True or \
        not grade[len(grade)-2::] == "th" or \
        not 8 < int(grade[0:len(grade)-2]) < 12:
            print(f"{grade} is not valid grade")
            print(f"{isinstance(grade,str)} | {8 < int(grade[0:len(grade)-2]) < 12} | {grade[len(grade)-2::] }")
            return self.__age
        self.__grade = grade
    

test = Student("Alice")

test.name ="Bobby"
print(test)
test.name = 123
test.name = "James"
print(test.get_name)

student = Student("Alice")
student.grade = "13th"
print(student.grade)