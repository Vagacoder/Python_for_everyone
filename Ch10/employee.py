## class Employee for Ch10 p10.9

class Employee:
    
    def __init__(self, name, salary):
        
        self._name = name
        self._salary = salary
        
    def __repr__init(self):
        return self._name + ', ' + str(self._salary)
        

class Manager(Employee):
    
    def __init__(self, name, salary, department):
        
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return self._name + ', ' + self._department + ', ' + str(self._salary)
        

class Excutive(Manager):
    
    def __init__(self, name, salary, department):
        
        super().__init__(name, salary, department)

    def __repr__(self):
        return self._name + ', ' + self._department + ', ' + str(self._salary)
    