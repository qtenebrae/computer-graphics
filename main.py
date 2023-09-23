from tkinter import *

root = Tk()

import tkinter.font as tkFont

myFont = tkFont.Font(family='Bahnschrift', size=16, weight='bold')

root.resizable(False, False)
root.title('Computer Graphics')

pict = Frame(root)
manage = Frame(root)

pict.pack(side=LEFT)
manage.pack(side=RIGHT)

canvas = Canvas(pict, width=900, height=900)
canvas.create_rectangle(0, 0, 900, 900, outline='#fff', fill='#fff')
canvas.pack(fill=BOTH, expand=1)

var_axleA = IntVar()
var_axleA.set(300)
var_axleB = IntVar()
var_axleB.set(200)
var_coordX = IntVar()
var_coordX.set(450)
var_coordY = IntVar()
var_coordY.set(450)
var_step = IntVar()
var_step.set(10)

axleA = Label(manage, text='Полуось A', font=myFont)
valueAxleA = Entry(manage, width=20, font=myFont, textvariable=var_axleA)

axleB = Label(manage, text='Полуось B', font=myFont)
valueAxleB = Entry(manage, width=20, font=myFont, textvariable=var_axleB)

coordCenter = Label(manage, text='Координаты центра', font=myFont)
coordX = Entry(manage, width=3, font=myFont, textvariable=var_coordX)
coordY = Entry(manage, width=3, font=myFont, textvariable=var_coordY)

step = Label(manage, text='Шаг', font=myFont)
valueStep = Entry(manage, width=5, font=myFont, textvariable=var_step)

coordCenter.pack()
coordX.pack(pady=10)
coordY.pack(pady=[10, 20])

axleA.pack()
valueAxleA.pack()
axleB.pack(pady=10)
valueAxleB.pack(pady=[10, 20])

step.pack(pady=10)
valueStep.pack(pady=[10, 20])

figure = None


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


firstCoord = Coord(0, 0)
secondCoord = Coord(10, 10)
colors = ["grey70", "yellow", "red", "green", "blue", "pink"]
currentColors = 0


def paint(event):
    global figure, firstCoord, secondCoord
    a = int(valueAxleA.get())
    b = int(valueAxleB.get())
    x = int(var_coordX.get())
    y = int(var_coordY.get())
    firstCoord.x = x - a / 2
    firstCoord.y = y - b / 2
    secondCoord.x = x + a / 2
    secondCoord.y = y + b / 2
    if figure is None:
        figure = canvas.create_oval(firstCoord.x, firstCoord.y, secondCoord.x, secondCoord.y,
                                    fill=colors[currentColors],
                                    outline='white')
    else:
        canvas.coords(figure, firstCoord.x, firstCoord.y, secondCoord.x, secondCoord.y)


starterButton = Button(manage, text="Рисовать", font=myFont)
starterButton.bind('<Button-1>', paint)
starterButton.pack(pady=10)


def on_key_press(event):
    global figure, firstCoord, secondCoord, currentColors
    if figure is None:
        return
    step = int(valueStep.get())
    if event.keysym == 'Left':
        canvas.coords(figure, firstCoord.x - step, firstCoord.y, secondCoord.x - step, secondCoord.y)
        firstCoord.x -= step
        secondCoord.x -= step
    elif event.keysym == 'Right':
        canvas.coords(figure, firstCoord.x + step, firstCoord.y, secondCoord.x + step, secondCoord.y)
        firstCoord.x += step
        secondCoord.x += step
    elif event.keysym == 'Up':
        canvas.coords(figure, firstCoord.x, firstCoord.y - step, secondCoord.x, secondCoord.y - step)
        firstCoord.y -= step
        secondCoord.y -= step
    elif event.keysym == 'Down':
        canvas.coords(figure, firstCoord.x, firstCoord.y + step, secondCoord.x, secondCoord.y + step)
        firstCoord.y += step
        secondCoord.y += step
    elif event.keysym == 'bracketleft':
        if currentColors != 0:
            currentColors -= 1
        else:
            currentColors = len(colors) - 1
        canvas.itemconfig(figure, fill=colors[currentColors])
    elif event.keysym == 'bracketright':
        if currentColors != len(colors) - 1:
            currentColors += 1
        else:
            currentColors = 0
        canvas.itemconfig(figure, fill=colors[currentColors])


root.bind('<KeyPress>', on_key_press)

root.mainloop()
