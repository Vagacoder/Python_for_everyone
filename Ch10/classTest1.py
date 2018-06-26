# -*- coding: utf-8 -*-

# super class
class Question:
    
    def __init__(self):
        self._value =0
    
    def display(self):
        print(self._value)

    def getData(self):
        raise NotImplementedError

# subclass inherited the class of Question        
class MQuestion(Question):
    
    def __init__(self):
        super().__init__()
        self._name = "MQ"

    def display(self):
        print(self._name)

    def getData(self):
        print(self._value)
        
        
# testing        
print("Start")
q1 = Question()
q2 = MQuestion()

# isinstance method 
print(isinstance(q1, MQuestion))
print(isinstance(q1, Question))
print(isinstance(q2, MQuestion))
print(isinstance(q2, Question))

# method polymorphsim
q1.display()
q2.display()

# abstract method 
# q1.getData()
q2.getData()