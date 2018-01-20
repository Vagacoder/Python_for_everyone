## class geometry for Ch09 P9.14

from math import pi, sqrt

class Geometry:
    
    def __init__(self, r = 0.0, h = 0.0):
        
        self._radius = r
        self._height = h
        
    def sphereVolume(self):
        sphVol = 4/3*pi*self._radius**3
        return sphVol
    
    def sphereSurface(self):
        sphSurf = 4* pi * self._radius **2
        return sphSurf
    
    def cylinderVolume(self):
        cylVol = pi*self._radius**2*self._height
        return cylVol
    
    def cylinderSurface(self):
        cylSurf = 2*pi*self._radius**2 + 2*pi*self._radius*self._height
        return cylSurf
    
    def coneVolume(self):
        coneVol = 1/3*pi*self._radius**2*self._height
        return coneVol
        
    def coneSurface(self):
        coneSurf = pi* self._radius* (self._radius + sqrt(self._height**2 + self._radius**2))
        + pi*self._radius**2
        return coneSurf


