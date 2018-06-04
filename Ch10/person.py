## supclass Person for Ch10 P10.8

class Person:
    
    def __init__(self, name, year):
        self._name = name
        self._DOB = year
        
    def __repr__(self):
        print(self._name +', ' + str(self._DOB))
    

class Student(Person):
    
    def __init__(self, name, year, major):
        super().__init__(name, year)
        self._major = major
    
    def __repr__(self):
        return self._name +', ' + str(self._DOB) + ', ' + self._major
        

class Instructor(Person):
    
    def __init__(self, name, year, salary):
        
        super().__init__(name, year)
        self._salary = salary
    
    def __repr__(self):
        return self._name +', ' + str(self._DOB) + ', ' + str(self._salary)
