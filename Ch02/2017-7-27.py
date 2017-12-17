## Ch02 P2.30
from graphics import *

win = GraphWin('P2.30',600,400)
win.setBackground('white')

cir1 = Circle(Point(150,150),75)
cir1.setWidth(15)
cir1.setOutline('blue')


cir2 = Circle(Point(320,150),75)
cir2.setWidth(15)
cir2.setOutline('black')

cir3 = Circle(Point(490,150),75)
cir3.setWidth(15)
cir3.setOutline('red')

cir4 = Circle(Point(235,230),75)
cir4.setWidth(15)
cir4.setOutline('yellow')

cir5 = Circle(Point(410,230),75)
cir5.setWidth(15)
cir5.setOutline('green')

cir1.draw(win)
cir2.draw(win)
cir3.draw(win)
cir4.draw(win)
cir5.draw(win)

win.getMouse()
