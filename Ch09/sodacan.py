## Ch09 class SodaCan for P9.5

import math

class SodaCan:
    
    def __init__(self, height = 0.0, radius = 0.0):
        self._height = height
        self._radius = radius
    
    def getSurfaceArea(self):
        surfaceArea = (2.0 * math.pi * self._radius * self._height) + (math.pi * self._radius **2) 
        return surfaceArea
    
    def getVolume(self):
        volume = math.pi * self._radius**2 * self._height
        return volume
        
    
        