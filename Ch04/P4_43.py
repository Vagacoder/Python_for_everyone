# -*- coding: utf-8 -*-
## P4.43
"""
Created on Wed Jun  6 16:43:14 2018

@author: qhu
"""

from ezgraphics import GraphicsWindow

window = GraphicsWindow(800, 600)
canvas = window.canvas()

x_int = 400
y_int = 300
old_x = x_int
old_y = y_int
cur_x = x_int
cur_y = y_int
increment = 10

for i in range(1, 20, 1):
    cur_x = cur_x + (-1)**(i+1)*increment*i
    canvas.drawLine(old_x, old_y, cur_x, cur_y)
    old_x = cur_x
    
    cur_y = cur_y + (-1)**(i+1)*increment*i
    canvas.drawLine(old_x, old_y, cur_x, cur_y)
    old_y = cur_y

window.wait()