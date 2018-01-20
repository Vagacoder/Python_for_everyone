## CH09 P9.30

from resistor import Resistor

r1 = Resistor(6.2, 5)
print(r1.getNominal())
print(r1.getTolerance())
print(r1.getActualResistance())
print(r1.colorDecode('Red','Violet','Green','Gold'))
