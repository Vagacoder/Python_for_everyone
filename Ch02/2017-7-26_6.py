## Ch02 P2.27 "House"

from graphics import *

win = GraphWin('P2.27',400,600)
win.setBackground('#00FFFF')

tri1 = Polygon(Point(150,150), Point(50,250), Point(250,250))       #front roof
tri1.setFill('red')

rec1 = Rectangle(Point(50,250),Point(250,400))          #front wall
rec1.setFill('#FFF8DC')

rec2 = Rectangle(Point(90,300),Point(130,400))          #door
rec2.setFill('lime')

rec3 = Rectangle(Point(170,300), Point(220,350))        #window
rec3.setFill('orange')

pol1 = Polygon(Point(150,150),Point(275,100),Point(375,200),Point(250,250))     #side roof
pol1.setFill('red')

pol2 = Polygon(Point(250,250), Point(375,200),Point(375,350),Point(250,400))    #side wall
pol2.setFill('#FFF8DC')

pol3 = Polygon(Point(300,280),Point(350,260),Point(350,310),Point(300,330))         #side window
pol3.setFill('orange')


tri1.draw(win)
rec1.draw(win)
rec2.draw(win)
rec3.draw(win)
pol1.draw(win)
pol2.draw(win)
pol3.draw(win)

win.getMouse()
