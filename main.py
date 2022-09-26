from tkinter import *
from pyscreenshot import grab
from mnistModel import eval, evalAvg
from PIL import Image, ImageChops, ImageOps
import math
import random

WIDTH, HEIGHT = 300, 300
DIMENSIONS = str(WIDTH)+'x'+str(HEIGHT)

window = Tk()

window.geometry(DIMENSIONS)
window.resizable(False, False)

posRight, posDown = int(window.winfo_screenwidth() / 2 - WIDTH / 2), int(window.winfo_screenheight() / 2 - HEIGHT / 2)
window.geometry("+{}+{}".format(posRight, posDown))

frame = Frame(window)
frame.pack(expand=True, fill=BOTH)

def trim(im):
    bg = Image.new("RGB", im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im.convert("RGB"), bg)
    diff = ImageChops.add(diff, diff)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    else: 
        return im

def mouseClick(event):
    filename = 'digitDrawing.png'
    img = grab(bbox=(posRight+5, posDown+75, posRight+WIDTH-5, posDown+HEIGHT))
    img = trim(img)
    maxwh = max(img.width, img.height)
    img = img.resize((maxwh, maxwh))
    img.show()
    img.save(filename)
    eval(filename)
    canvas.delete("all")

button1 = Button(frame, text="Finish/Clear")
button1.pack(side=TOP)
button1.bind("<Button>", mouseClick) 

canvas = Canvas(frame, width=WIDTH, height=HEIGHT, bg='gray1')
canvas.pack()
canvas.old_coords = None

def start(event):
    canvas.old_coords = event.x, event.y

def end(event):
    canvas.old_coords = None

def move(event):
    x, y = event.x, event.y
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1, width=WIDTH/30, fill='mediumpurple1', capstyle=ROUND, smooth=TRUE, splinesteps=36)
    canvas.old_coords = x, y

canvas.bind('<Button-1>', start)
canvas.bind('<B1-Motion>', move)
canvas.bind('<ButtonRelease-1>', end)

window.mainloop()

