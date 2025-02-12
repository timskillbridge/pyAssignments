from __future__ import annotations

def compare_dict_to_class(testDict,testClass):
    keys = {}
    for x,y in enumerate([key for key in testClass.__dict__.keys()]):
        keys[y[1::]] = x
    # print(f"{type(keys.keys())} : {keys}")
    # print(f"{type(testDict)} : {testDict}")
    return keys.keys() == testDict.keys()

class Student:
    student_body = {}
    faculty_roster = {}
    def __init__(self,f_name:str, l_name:str, age:int, grade:str):
        self._f_name = f_name
        self._l_name = l_name
        self._age = age
        self._grade = grade

    @classmethod
    def add_student(cls,student):
        if compare_dict_to_class(student,cls("dummy","dummy",12,"dummy")) == False:
            print("Invalid Student")
            return False
        if len(cls.student_body) == 0:
            cls.student_body[1] = cls(**student)
        else: cls.student_body[max(cls.student_body.keys())+1] = cls(**student)
    
    # @classmethod
    # def add_faculty(cls,faculty):
    #     if compare_dict_to_class(faculty,cls("dummy","dummy",12,"dummy")) == False:
    #         print("Invalid faculty")
    #         return False
    #     if len(cls.faculty_roster.role[job]) == 0:
    #         cls.student_body[1] = cls(**student)
    #     else: cls.student_body[max(cls.student_body.keys())+1] = cls(**student)
    
    # @property
    def __repr__(self):
        return f"{self._f_name} is {self._age} years old and in {self._grade} grade"

    @property
    def get_name(self):
        return self.__name__
    
    @get_name.setter
    def set_name(self,newName):
        self._name = newName


school = Student("Dummy","Data",99,"9th")
james = {"f_name":"James","l_name" : "Smith","age":14,"grade" : "11th"}

school.add_student(james)
print(school.student_body)