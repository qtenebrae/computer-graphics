from tkinter import *

import tkinter.font as tkFont


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class App(Tk):
    def __init__(self, resizeable=False):
        Tk.__init__(self)
        self.title("Oval")
        self.font = tkFont.Font(family='Bahnschrift', size=16, weight='bold')

        self.pict = Frame(self)
        self.manage = Frame(self)
        self.pict.pack(side=LEFT)
        self.manage.pack(side=RIGHT)

        self.canvas = Canvas(self.pict, width=900, height=900)
        self.canvas.create_rectangle(0, 0, 900, 900, outline='#fff', fill='#fff')
        self.canvas.pack(fill=BOTH, expand=1)

        self.var_axleA = IntVar()
        self.var_axleA.set(300)
        self.var_axleB = IntVar()
        self.var_axleB.set(200)
        self.var_coordX = IntVar()
        self.var_coordX.set(450)
        self.var_coordY = IntVar()
        self.var_coordY.set(450)
        self.var_step = IntVar()
        self.var_step.set(10)

        self.axleA = Label(self.manage, text='Полуось A', font=self.font)
        self.valueAxleA = Entry(self.manage, width=10, textvariable=self.var_axleA, font=self.font)

        self.axleB = Label(self.manage, text='Полуось B', font=self.font)
        self.valueAxleB = Entry(self.manage, width=10, textvariable=self.var_axleB, font=self.font)

        self.coordCenter = Label(self.manage, text='Координаты центра', font=self.font)
        self.coordX = Entry(self.manage, width=3, textvariable=self.var_coordX, font=self.font)
        self.coordY = Entry(self.manage, width=3, textvariable=self.var_coordY, font=self.font)

        self.step = Label(self.manage, text='Шаг', font=self.font)
        self.valueStep = Entry(self.manage, width=5, textvariable=self.var_step, font=self.font)

        self.coordCenter.pack()
        self.coordX.pack(pady=10)
        self.coordY.pack(pady=[10, 20])

        self.axleA.pack()
        self.valueAxleA.pack()
        self.axleB.pack(pady=10)
        self.valueAxleB.pack(pady=[10, 20])

        self.step.pack(pady=10)
        self.valueStep.pack(pady=[10, 20])

        self.firstCoord = Coord(0, 0)
        self.secondCoord = Coord(10, 10)
        self.colors = ["grey", "yellow", "red", "green", "blue", "pink"]
        self.currentColors = 0

        self.figure = None

        self.starterButton = Button(self.manage, text="Рисовать", font=self.font)
        self.starterButton.bind('<Button-1>', self.paint)
        self.starterButton.pack(pady=10)

        self.bind('<KeyPress>', self.on_key_press)

    def paint(self, event):
        a = int(self.valueAxleA.get())
        b = int(self.valueAxleB.get())
        x = int(self.var_coordX.get())
        y = int(self.var_coordY.get())
        self.firstCoord.x = x - a / 2
        self.firstCoord.y = y - b / 2
        self.secondCoord.x = x + a / 2
        self.secondCoord.y = y + b / 2
        if self.figure is None:
            self.figure = self.canvas.create_oval(self.firstCoord.x, self.firstCoord.y, self.secondCoord.x,
                                                  self.secondCoord.y,
                                                  fill=self.colors[self.currentColors],
                                                  outline='white')
        else:
            self.canvas.coords(self.figure, self.firstCoord.x, self.firstCoord.y, self.secondCoord.x,
                               self.secondCoord.y)

    def on_key_press(self, event):
        if self.figure is None:
            return
        step = int(self.valueStep.get())
        if event.keysym == 'Left':
            self.canvas.coords(self.figure, self.firstCoord.x - step, self.firstCoord.y, self.secondCoord.x - step,
                               self.secondCoord.y)
            self.firstCoord.x -= step
            self.secondCoord.x -= step
        elif event.keysym == 'Right':
            self.canvas.coords(self.figure, self.firstCoord.x + step, self.firstCoord.y, self.secondCoord.x + step,
                               self.secondCoord.y)
            self.firstCoord.x += step
            self.secondCoord.x += step
        elif event.keysym == 'Up':
            self.canvas.coords(self.figure, self.firstCoord.x, self.firstCoord.y - step, self.secondCoord.x,
                               self.secondCoord.y - step)
            self.firstCoord.y -= step
            self.secondCoord.y -= step
        elif event.keysym == 'Down':
            self.canvas.coords(self.figure, self.firstCoord.x, self.firstCoord.y + step, self.secondCoord.x,
                               self.secondCoord.y + step)
            self.firstCoord.y += step
            self.secondCoord.y += step
        elif event.keysym == 'bracketleft':
            if self.currentColors != 0:
                self.currentColors -= 1
            else:
                self.currentColors = len(self.colors) - 1
            self.canvas.itemconfig(self.figure, fill=self.colors[self.currentColors])
        elif event.keysym == 'bracketright':
            if self.currentColors != len(self.colors) - 1:
                self.currentColors += 1
            else:
                self.currentColors = 0
            self.canvas.itemconfig(self.figure, fill=self.colors[self.currentColors])


app = App()
app.mainloop()
