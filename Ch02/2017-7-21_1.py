from graphics import *
def main():
    win = GraphWin("My Circle", 400, 400)
    c = Circle(Point(200,200), 100)
    c.draw(win)
    win.getMouse() # pause for click in window
    win.close()
main()
