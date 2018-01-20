## class moth for Ch09 P9.13

class Moth:
    
    def __init__(self):
        self._position = 0.0
        
    
    def getPosition(self):
        return self._position
    
    
    def moveToLight(self, lightPosition):
        self._position = (self._position + lightPosition) /2.0
        