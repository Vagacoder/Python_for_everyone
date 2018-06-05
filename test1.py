from math import sqrt, pi

print(sqrt(2))
print(2**0.5)
print(pi)

print('-'*100)
name= "No"
id = 1023
print(name + str(id))

from ezgraphics import *

w = GraphicsWindow(400, 400)
c = w.canvas()
c.drawRectangle(100,40, 30,50)
w.wait()

if 3> 10:
    print("Yes")
else:
    print("No")

