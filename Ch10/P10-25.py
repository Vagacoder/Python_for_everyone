# -*- coding: utf-8 -*-
## P10.25 

class Circuit:
    
    def __init__(self, resistance = 0):
        self._resistance = resistance

    def getResistance(self):
        return self._resistance

    
class Resistor(Circuit):
    
    def __init__(self, resistance =0):
        super().__init__(resistance)
    

class Serial(Circuit):
    
    def __init__(self):
        super().__init__()
        self._circuitList = list()
        
    def addCircuit(self, new_circuit):
        self._circuitList.append(new_circuit)
        
    def getResistance(self):
        
        totalResis = 0
        for c in self._circuitList:
            totalResis += c.getResistance()
        return totalResis

        
class Parallel(Circuit):
    
    def __init__(self):
        super().__init__()
        self._circuitList = list()
    
    def addCircuit(self, new_circuit):
        self._circuitList.append(new_circuit)
        
    def getResistance(self):
        totalResis = 0
        for c in self._circuitList:
            totalResis += 1/c.getResistance()
        return 1/totalResis    
        
        
def main():
    r1 = Resistor(5)
    r2 = Resistor(10)
    r3 = Resistor(15)
    s1 = Serial()
    s1.addCircuit(r1)
    s1.addCircuit(r2)
    s1.addCircuit(r3)
    print(s1.getResistance())
    p1 = Parallel()
    p1.addCircuit(r1)
    p1.addCircuit(r2)
    print(p1.getResistance())
    p1.addCircuit(s1)
    print(p1.getResistance())

main()