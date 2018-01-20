## Ch09 P9.31

from resistor import Resistor
from voltagedivider import VoltageDivider

for i in range(10):
    r1 = Resistor(250, 5)
    r2 = Resistor(750, 5)
    v1 = VoltageDivider(r1, r2)
    print(v1.getNominalGain())
    print(v1.getActualGain())