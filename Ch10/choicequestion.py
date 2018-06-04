# -*- coding: utf-8 -*-

from questions import Question

class ChoiceQuestion(Question):
    
    def __init__(self):
        super().__init__()
        
    def display(self):
        
        print('This is a choice question.')
        print(self._text)
        
    
