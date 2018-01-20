## For Ch09 P9.12

class Bug:
    
    def __init__(self, initialPosition):
        self._position = initialPosition
        self._direction = 1
    
    def turn(self):
        self._direction = - self._direction
    
    def move(self):
        self._position += self._direction
    
    def getPosition(self):
        return self._position
    