# https://coderslegacy.com/python/tkinter-canvas/
# https://twitter.com/aemkei/status/1378106734871461890
from tkinter import *

def create_box(canvas, x, y):
    a = 4
    coord = x * a, y * a, x * a + a, y * a + a
    canvas.create_rectangle(
      coord,
      fill="grey"
    )

def draw_xor(canvas):
  for j in range(256):
    for i in range(256):
      if (i ^ j) % 9:
        create_box(canvas, i, j)

root = Tk()

frame = Frame(root, width=512, height=512)
frame.pack()
canvas = Canvas(frame, width=512, height=512)
canvas.pack()
draw_xor(canvas)

root.mainloop()
