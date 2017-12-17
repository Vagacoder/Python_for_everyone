## Ch02 R.23

from graphics import *

win = GraphWin('Ch02 R2.23', 400, 600)
win.setBackground('white')

oval1 = Oval(Point(20,20),Point(300,170))

rec1 = Rectangle(Point(20,20),Point(300,170))
rec1.setOutline('lime')
rec1.setWidth(3)

oval1.draw(win)
rec1.draw(win)

win.getMouse()
