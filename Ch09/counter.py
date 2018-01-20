## counter class for Ch09 P9.1 and P9.2

class Counter :
    def __init__(self):
        self._value = 0
        self._max = 0

    def getValue(self) :
        return self._value

    def click(self) :
        if self._value < self._max:
            self._value = self._value + 1
        else:
            print('Maximum limit reached! Please reset counter!')

    def reset(self) :
        self._value = 0
    
    def undo(self):
        if self._value > 0:
            self._value -= 1
    
    def setLimit(self, maximum):
        self._max = maximum
        
    def __repr__(self):
        return str(self._value)
        
