from graphics import GraphicsWindow
from sys import exit
win = GraphicsWindow()
canvas = win.canvas()
x = int(input("Please enter the x coordinate: "))
y = int(input("Please enter the y coordinate: "))
if x < 0 or y < 0 :
    exit("Error: x and y must be >= 0")
canvas.drawOval(x - 5, y - 5, 10, 10)
win.wait()