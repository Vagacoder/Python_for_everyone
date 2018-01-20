## class resistor for Ch09 P9.29

import random

class Resistor:
    
    def __init__(self, nominalValue, tolerance):

        self._colorTable = {'Black':[0, 1, 0], 'Brown':[1, 10, 1.0], 'Red': [2, 100, 2.0]
        ,'Orange': [3, 1000, 0], 'Yellow': [4, 10000, 0], 'Green': [5, 100000, 0.5],
        'Blue':[6, 1000000, 0.25], 'Violet':[7, 10000000, 0.1], 'Gray':[8, 100000000, 0.05],
        'White':[9, 1000000000, 0], 'Gold':[0, 0.1, 5], 'Silever':[0, 0.01, 10], '':[0,0,20]}
        
        self._nominalValue = nominalValue
        self._tolerance = tolerance
        maxValueVariable = self._nominalValue * self._tolerance/100.0
        valueVariable = random.random()* 2 * maxValueVariable - maxValueVariable
        self._actualValue = self._nominalValue + valueVariable
    
    def getNominal(self):
        return self._nominalValue
    
    def getTolerance(self):
        return self._tolerance
    
    def getActualResistance(self):
        return self._actualValue
    
    def colorDecode(self, first, second, third, forth):
        firstCode = self._colorTable[first][0]
        secondCode = self._colorTable[second][0]
        thirdCode = self._colorTable[third][1]
        forthCode = self._colorTable[forth][2]
        
        return str((firstCode * 10 + secondCode)* thirdCode) + ' +- ' + str(forthCode) +'% Om'