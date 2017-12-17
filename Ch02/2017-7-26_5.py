## Ch02 P2.26 "Bull's eye"

from graphics import *

win = GraphWin('P2.26',400,600)

cir1 = Circle(Point(200,300), 100)
cir1.setFill('black')

cir2 = Circle(Point(200,300), 80)
cir2.setFill('white')

cir3 = Circle(Point(200,300), 60)
cir3.setFill('black')

cir4 = Circle(Point(200,300), 45)
cir4.setFill('white')

cir5 = Circle(Point(200,300), 20)
cir5.setFill('black')


cir1.draw(win)
cir2.draw(win)
cir3.draw(win)
cir4.draw(win)
cir5.draw(win)

win.getMouse()
