## Class CannonBall for Ch09 P9.28

import math

class CannonBall:
    
    def __init__(self, x = 0.0):
        self._xPosition = x
        self._yPosition = 0.0
        self._xVelocity = 0.0
        self._yVelocity = 0.0
        self._G = -9.81
    
    def move(self, sec):
        self._xPosition += self._xVelocity * sec
        self._yPosition += (self._yVelocity * sec + 0.5 * self._G * sec **2)
        self._yVelocity += self._G * sec
        #print(self._yVelocity)
        
    def getX(self):
        return self._xPosition
    
    def getY(self):
        return self._yPosition
    
    def shoot(self, initialVelocity, angle):
        self._xVelocity = initialVelocity * math.cos(angle)
        self._yVelocity = initialVelocity * math.sin(angle)
        
        
        