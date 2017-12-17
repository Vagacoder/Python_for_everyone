## Ch2 2.6 Simple drawing

from graphics import *

win = GraphWin('Test', 400, 600)

rectan1= Rectangle(Point(0, 10),Point (100,20))
rectan1.setFill('red')

rectan2= Rectangle(Point(0, 30),Point (150,40))
rectan2.setOutline('red')
rectan2.setFill('lime')

rectan3= Rectangle(Point(0, 50),Point (75,60))
rectan3.setOutline('white')
rectan3.setFill('blue')

rectan1.draw(win)
rectan2.draw(win)
rectan3.draw(win)
