from tkinter import *

import tkinter.font as tkFont
from coord import Coord


class App(Tk):
    """Класс для создания и вызова экземпляра приложения tkinter

    Атрибуты:
        pict (Frame): фрейм для отображения рисунка.
        manage (Frame): фрейм для управления параметрами овала.
        canvas (Canvas): холст для рисования овала.
        var_axleA (IntVar): переменная для хранения значения полуоси A.
        var_axleB (IntVar): переменная для хранения значения полуоси B.
        var_coordX (IntVar): переменная для хранения значения координаты X центра овала.
        var_coordY (IntVar): переменная для хранения значения координаты Y центра овала.
        var_step (IntVar): переменная для хранения значения шага перемещения овала.
        axleA (Label): метка для отображения текста "Полуось A".
        valueAxleA (Entry): поле для ввода значения полуоси A.
        axleB (Label): метка для отображения текста "Полуось B".
        valueAxleB (Entry): поле для ввода значения полуоси B.
        coordCenter (Label): метка для отображения текста "Координаты центра".
        coordX (Entry): поле для ввода значения координаты X центра овала.
        coordY (Entry): поле для ввода значения координаты Y центра овала.
        step (Label): метка для отображения текста "Шаг".
        valueStep (Entry): поле для ввода значения шага перемещения овала.
        firstCoord (Coord): объект класса Coord для хранения координат первой точки овала.
        secondCoord (Coord): объект класса Coord для хранения координат второй точки овала.
        colors (list): список цветов для заливки овала.
        currentColors (int): индекс текущего цвета заливки овала.
        paintButton (Button): кнопка для запуска рисования овала.
        figure (int): идентификатор фигуры на холсте.

    Методы:
        set_coords()
            Считывает параметры из переменных *Var,
            вычисляет значения x,y для точек firstCoord и secondCoord,
            сохраняет вычисленные значения.
        paint(event)
            Обрабатывает нажатие кнопки paintButton,
            рисует фигуру, либо изменяет ее местоположение.
        on_key_press(event)
            Обрабатывает нажатия клавиш на клавиатуре,
            перемещает фигуру вниз/вверх/влево/вправо на заданный шаг,
            перекрашивает фигуру на следующий/предыдущий цвет.
    """

    def __init__(self):
        Tk.__init__(self)
        self.title("Oval")
        self.resizable(False, False)
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

        self.paintButton = Button(self.manage, text="Рисовать", font=self.font)
        self.paintButton.bind('<Button-1>', self.paint)
        self.paintButton.pack(pady=10)

        self.bind('<KeyPress>', self.on_key_press)

        self.figure = None

    def set_coords(self):
        """Метод для установки координат овала на холсте."""

        a = int(self.valueAxleA.get())
        b = int(self.valueAxleB.get())
        x = int(self.var_coordX.get())
        y = int(self.var_coordY.get())
        self.firstCoord.x = x - a / 2
        self.firstCoord.y = y - b / 2
        self.secondCoord.x = x + a / 2
        self.secondCoord.y = y + b / 2

    def paint(self, event):
        """Метод для отрисовки овала на холсте."""

        self.set_coords()
        if self.figure is None:
            self.figure = self.canvas.create_oval(self.firstCoord.x, self.firstCoord.y, self.secondCoord.x,
                                                  self.secondCoord.y,
                                                  fill=self.colors[self.currentColors],
                                                  outline='white')
        else:
            self.canvas.coords(self.figure, self.firstCoord.x, self.firstCoord.y, self.secondCoord.x,
                               self.secondCoord.y)

    def on_key_press(self, event):
        """Метод для обработки нажатий клавиш на клавиатуре.

        Аргументы:
            event (Event): объект события, содержащий информацию о нажатой клавише.

        Действия:
            - Если фигура не создана, метод завершает работу.
            - Если нажата клавиша "Left", фигура перемещается влево на значение шага.
            - Если нажата клавиша "Right", фигура перемещается вправо на значение шага.
            - Если нажата клавиша "Up", фигура перемещается вверх на значение шага.
            - Если нажата клавиша "Down", фигура перемещается вниз на значение шага.
            - Если нажата клавиша "bracketleft", цвет заливки фигуры изменяется на предыдущий цвет из списка цветов.
            - Если нажата клавиша "bracketright", цвет заливки фигуры изменяется на следующий цвет из списка цветов.
        """

        if self.figure is None:
            if event.keysym == "Return":
                self.paint(event)
            else:
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
