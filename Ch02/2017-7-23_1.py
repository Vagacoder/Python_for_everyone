## Ch02 P2.24

from graphics import *
#import time

win = GraphWin('P2.24', 400, 600)
win.setBackground('white')

rect1 = Rectangle(Point(30,30),Point(130,130))
rect1.setFill('pink')

rect2 = Rectangle(Point(30, 150),Point(130, 250))
rect2.setFill(color_rgb(200,0,255))

rect1.draw(win)
rect2.draw(win)

circle1 = Circle(Point(200,450),120)
circle1.setWidth(10)
circle1.setFill('yellow')

circle2 = Circle(Point(150,420),20)
circle2.setFill('red')
circle2.setOutline('yellow')
circle3 = Circle(Point(250,420),20)
circle3.setFill('red')
circle3.setOutline('yellow')

line1 = Line(Point(150,500),Point(250,500))
line1.setWidth((10))
line1.setFill('lime')

circle1.draw(win)
circle2.draw(win)
circle3.draw(win)
line1.draw(win)

win.getMouse()

