## Ch09 P9.9

from combolock import ComboLock

cl1 = ComboLock(10, 5, 10)
cl1.turnRight(10)
cl1.turnLeft(5)
cl1.turnRight(5)
print(cl1.open())