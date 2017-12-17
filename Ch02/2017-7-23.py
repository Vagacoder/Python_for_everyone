## Ch02 SC 27-32

from graphics import *

win = GraphWin('Test', 400, 600)
win.setBackground('lime')

rect1 = Rectangle(Point(20,20), Point(220,220))
rect1.setFill('red')
rect1.setOutline('cyan')

rect2 = Rectangle(Point(20, 250), Point(270,500))
rect2.setFill('white')
rect2.setOutline('tan')


rect1.draw(win)
rect2.draw(win)

oval1 = Oval(Point(20,20), Point(220,220))
oval1.setOutline('blue')
oval1.setFill('yellow')
oval2 = Oval(Point(20, 250), Point(270,500))
oval2.setFill('purple')

oval1.draw(win)
oval2.draw(win)

circle1 = Circle(Point(100,100),25)
circle1.setFill('orange')

circle1.draw(win)

line1 = Line(Point(100,100),Point(150,200))
line1.setArrow('both')
line1.setFill('green')
line2 = Line(Point(150,200),Point(200,100))
line2.setArrow('first')
line2.setOutline('lime')

line1.draw(win)
line2.draw(win)

text1 = Text(Point(300,400),'Hello world')
text1.setFill('blue')
text2 = Text(Point(300,200),'Welcome')
text2.setSize(20)
text2.setFace('courier')
text2.setStyle('bold')
#text2.setStyle('italic')

rect3 = Rectangle(Point(300,100),Point(360,120))
rect3.setFill('blue')
centerRect3 = rect3.getCenter()
#print(centerRect3)

text3 = Text(centerRect3,'Qirui Hu')
text3.setFill('red')


rect3.draw(win)

text1.draw(win)
text2.draw(win)
text3.draw(win)

