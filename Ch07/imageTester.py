from ezgraphics import *

imgWin = ImageWindow()

for row in range(200):
    for col in range(0, row):

        imgWin.setPixel(row, col, 255, 0, 0)
        imgWin.setPixel(200 - row, 200 - col, 0, 255, 0)

imgWin.wait()