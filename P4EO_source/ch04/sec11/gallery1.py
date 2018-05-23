from ezgraphics import GraphicsWindow, GraphicsImage

GAP = 10
NUM_PICTURES = 20
MAX_WIDTH = 720

win = GraphicsWindow(MAX_WIDTH, 700)
canvas = win.canvas()

pic = GraphicsImage("picture1.gif")
canvas.drawImage(0, 0, pic)

win.wait()
