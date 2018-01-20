## class VoltageDivider for Ch09 P9.31

#from resistor import Resistor

class VoltageDivider:
    
    def __init__(self, resistor1, resistor2):
        
        self._nominalResistance1 = resistor1.getNominal()
        self._nominalResistance2 = resistor2.getNominal()
        self._actualResistance1 = resistor1.getActualResistance()
        self._actualResistance2 = resistor2.getActualResistance()
    
    
    def getNominalGain(self):
        
        return self._nominalResistance2 /(self._nominalResistance1 + self._nominalResistance2)
    
    
    def getActualGain(self):
        
        return self._actualResistance2 / (self._actualResistance1 + self._actualResistance2)