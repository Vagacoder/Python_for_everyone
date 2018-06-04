## Class NumericQuestion for Ch10 P10.1

from questions import Question

class NumericQuestion(Question):

    def __init__(self):
        super().__init__()
    
    def checkAnswer(self, response) :
        
        if abs(response - self._answer) < 0.01 :
            return True
        else:
            return False