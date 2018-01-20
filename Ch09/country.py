## class country for ch09 P9.23

class Country:
    
    def __init__(self, name = '', pop = 0, area = 0):
        self._name = name
        self._pop = pop
        self._area = area
        self._density = 0.0
    
    def setPop(self, pop):
        self._pop = pop
    
    def setArea(self, area):
        self._area = area
    
    def getName(self):
        return self._name
    
    def getPop(self):
        return self._pop
    
    def getArea(self):
        return self._area
    
    def getDensity(self):
        if self._area != 0:
            return self._pop / self._area
        else:
            return 0.0
        
    
    