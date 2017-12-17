## P4.39
from graphics import *

win = GraphWin('P4.39', 600, 600)
win.setBackground('White')

X_INI = 100
Y_INI = 100
L = 50

for i in range(0,8):
    for j in range(0,8):
        rec = Rectangle(Point(X_INI + j*L,Y_INI +i*L), Point(X_INI + (j+1)*L , Y_INI + (i+1)*L ))
        rec_old = rec.clone()
        if (i+j)%2 == 0:
            rec_old.setFill('black')
        rec_old.draw(win)


win.getMouse()

## P4.40
from graphics import *
from math import *

win = GraphWin('P4.39', 600, 600)
win.setBackground('White')

X_INI = 50
Y_INI = 300

L = 500/2/pi
A = 150
n = 200

DELTA = 2*pi*L/n

for i in range(n):
    x = i*DELTA
    y = A * sin(2*pi/n*i)
    line = Line(Point(X_INI + x,Y_INI), Point(X_INI + x, Y_INI - y))
    line_old = line.clone()
    line_old.setFill('red')
    line_old.draw(win)

win.getMouse()

## P4.42
from graphics import *
from math import *

win = GraphWin('P4.41', 600, 600)
win.setBackground('white')

X_INI = 300
Y_INI = 300

for i in range(1000):
    theta = i * 2*pi/1000
    r = 200*cos(2*theta)
    x = r*cos(theta)
    y = r*sin(theta)
    point = Point(X_INI + x, Y_INI - y)
    point_old = point.clone()
    point_old.draw(win)

win.getMouse()

## P4.41
from graphics import *
from math import *

win = GraphWin('P4.41', 800,800)
win.setBackground('white')

X_INI = 50
Y_INI = 750

x_lower = 50
x_upper = 550

line1 = Line(Point(X_INI, Y_INI), Point(X_INI, 50))
line2 = Line(Point(X_INI, Y_INI), Point(750, Y_INI))
line1.setArrow('last')
line2.setArrow('last')

line1.draw(win)
line2.draw(win)

for i in range((x_upper - x_lower)*10):
    delta_x = i * 1/10
    x = x_lower + delta_x
    y = 0.00005 * x**3 - 0.03 * x**2 +4*x +200
    point = Point(X_INI + x , Y_INI - y)
    point_old = point.clone()
    point_old.draw(win)

win.getMouse()

## P4.43
from graphics import *
from math import *

win = GraphWin('P4.43', 800,800)
win.setBackground('white')

X_INI = 400
Y_INI = 400

width = 20

x = X_INI
y = Y_INI

for i in range(1,16):
    increase = (-1)**(i+1)*i*width
    x1 = x + increase
    y1 = y
    x2 = x1
    y2 = y1 -increase
    line1 = Line(Point(x, y), Point(x1, y1))
    line2 = Line(Point(x1, y1), Point(x2, y2))
    line1_old = line1.clone()
    line2_old = line2.clone()
    line1_old.draw(win)
    line2_old.draw(win)
    x = x2
    y = y2

win.getMouse()
