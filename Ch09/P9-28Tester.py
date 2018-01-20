## Ch09 P9.28

from cannonball import CannonBall
import math

b1 = CannonBall(0)
b1.shoot(100, math.pi/6.0)
time = 0.0
YcloseToZero = 0
b1.move(0.001)
while YcloseToZero < 2:
    b1.move(0.001)
    time += 0.001
    if abs(b1.getY()) < 0.1:
        YcloseToZero +=1
#    print(time)
#    print(b1.getX())
#    print(b1.getY())
#    print()

print(time)
print(b1.getX())
print(b1.getY())
