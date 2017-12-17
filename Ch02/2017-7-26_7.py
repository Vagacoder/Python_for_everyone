## Ch02 P2.28

from graphics import *

win = GraphWin('P2.28',400,400)

line1 = Line(Point(50,50),Point(250,50))    # x axis
line1.setArrow('last')

line2 = Line(Point(50,50),Point(50,250))    # y axis
line2.setArrow('last')

line3 = Line(Point(100,45),Point(100,55))   # x axis tick
line4 = Line(Point(150,45),Point(150,55))
line5 = Line(Point(200,45),Point(200,55))

line6 = Line(Point(45,100),Point(55,100))   # y axis tick
line7 = Line(Point(45,150),Point(55,150))
line8 = Line(Point(45,200),Point(55,200))

text1 = Text(Point(50,35),'(0,0)')
text2 = Text(Point(220,35),'x')
text3 = Text(Point(40,220), 'y')

text4 = Text(Point(180,100),'(20,10)')
text5 = Text(Point(130,150),'(10,20)')

point1 = Circle(Point(150,100),2)
point1.setFill('red')
point1.setOutline('red')
point2 = Circle(Point(100,150),2)
point2.setFill('red')
point2.setOutline('red')

line1.draw(win)
line2.draw(win)
line3.draw(win)
line4.draw(win)
line5.draw(win)
line6.draw(win)
line7.draw(win)
line8.draw(win)

text1.draw(win)
text2.draw(win)
text3.draw(win)
text4.draw(win)
text5.draw(win)

point1.draw(win)
point2.draw(win)

win.getMouse()