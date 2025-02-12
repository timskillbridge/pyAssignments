from __future__ import annotations

def compare_dict_to_class(testDict,testClass):
    keys = {}
    for x,y in enumerate([key for key in testClass.__dict__.keys()]):
        keys[y[1::]] = x
    # print(f"{type(keys.keys())} : {keys}")
    # print(f"{type(testDict)} : {testDict}")
    return keys.keys() == testDict.keys()

class School:
    student_body = {}
    faculty_roster = {}
    def __init__(self,f_name:str, l_name:str, age:int, role:str, specialty:str, sex:str, salary=0):
        self._f_name = f_name
        self._l_name = l_name
        self._age = age
        self._role = role
        self._specialty = specialty
        self._sex = sex
        self._salary = salary

    @classmethod
    def add_student(cls,who):
        if compare_dict_to_class(who,cls("dummy","dummy",12,"dummy", "dummy","dummy")) == False:
            print("Invalid Entry")
            return False
        
        if len(cls.student_body) == 0:
            cls.student_body[1] = cls(**who)
        else: cls.student_body[max(cls.student_body.keys())+1] = cls(**who)
    
    def __repr__(self):
        return (
            f"{self._f_name} {self._l_name} is a {self._role}. "
            f"{'He ' if {self._sex} != "M" else 'She '}"
            f"{'teaches ' if {self._role} == 'Teacher' else 'is in the '}"
            f"{self._specialty} grade\n"
        )

    @property
    def get_name(self):
        return self.__name__
    
    @get_name.setter
    def set_name(self,newName):
        self._name = newName


school = School("first","last",99,"student", "11th", "X",0)
james = {"f_name":"James","l_name" : "Smith","age":14,"role" : "student", "specialty":"11th", "sex":"M","salary":0}
mr_smith = {"f_name":"fred","l_name" : "Smith","age":44,"role" : "Teacher", "specialty":"11th", "sex":"M","salary":0}

school.add_student(james)
school.add_student(mr_smith)
print(school.student_body)