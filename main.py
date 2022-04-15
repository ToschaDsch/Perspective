# This is a sample Python script.
import math
from tkinter import *
from math import asin

# global variable
color_axes = '#000000'
color_line = '#374534'
color_sin = '#ad1111'
color_arcsin = '#2311ad'

canvas = Canvas()
canvas_height = 800
canvas_width = 800
x0 = canvas_width / 2
y0 = canvas_width * 1 / 3

r = 1
n = 10
h = 1


class GeometryObject:
    def __init__(self, fild_or_cylinder, row, step, height, radius, line_notLine_notLine2):
        self.fild_or_cylinder = fild_or_cylinder
        self.row = row
        self.step = step
        self.height = height
        self.radius = radius
        self.line_notLine_notLine2 = line_notLine_notLine2
        self.coordinate_x = [[0] * (self.row + 1) for i in range(2 * (self.row + 1))]
        self.coordinate_y = [[0] * (self.row + 1) for i in range(2 * (self.row + 1))]
        self.coordinate_z = [[0] * (self.row + 1) for i in range(2 * (self.row + 1))]

        # make coordinate
        if self.fild_or_cylinder == "fild":
            self.make_field()
        else:
            self.make_cylinder()

        # make 2d projection and draw it
        if self.line_notLine_notLine2 == "line":
            self.make_2d_line()
        elif self.line_notLine_notLine2 == "notLine":
            self.make_2d_notLine()
        else:
            self.make_2d_notLine2()

    def make_2d_line(self):
        x2d = []
        y2d = []
        for k in range(0, 2*(self.row + 1)):
            for i in range(0, (self.row + 1)):
                if self.coordinate_z[k][i] == 0:
                    z = 0.1
                else:
                    z = self.coordinate_z[k][i]
                x = self.coordinate_x[k][i] * self.radius / z
                y = self.coordinate_y[k][i] * self.radius / z
                x2d.append(x)
                y2d.append(y)

            self.draw_a_line_from_array(x2d, y2d)
            x2d = []
            y2d = []

    def make_2d_notLine(self):
        pass


    def make_2d_notLine2(self):
        pass

    def make_field(self):
        k = 0
        # make vertical lines (direction z)
        for i in range(int(-self.row / 2), int(self.row / 2) + 1):
            for j in range(0, self.row + 1):
                x = i * self.step
                y = self.height
                z = j * self.step
                self.coordinate_x[k][j] = x
                self.coordinate_y[k][j] = y
                self.coordinate_z[k][j] = z
            k += 1

        # make horizontal lines (direction x)
        for j in range(0, self.row + 1):
            t = 0
            for i in range(int(-self.row / 2), int(self.row / 2) + 1):
                x = i * self.step
                y = self.height
                z = j * self.step
                self.coordinate_x[k][t] = x
                self.coordinate_y[k][t] = y
                self.coordinate_z[k][t] = z
                t += 1
            k += 1

    @staticmethod
    def draw_a_line_from_array(array_x, array_y):
        global x0, y0
        global canvas
        x1 = array_x[0]
        y1 = array_y[0]
        for index in range(1, len(array_x)):
            x2 = array_x[index]
            y2 = array_y[index]
            canvas.create_line(x1 + x0, y1 + y0,
                               x2 + x0, y2 + y0,
                               fill=color_line)

    def make_cylinder(self):
        pass


def init_canvas():
    global canvas, canvas_height, canvas_width
    master = Tk()
    canvas = Canvas(master,
                    width=canvas_width,
                    height=canvas_height)
    canvas.pack()


def draw_axes():
    canvas.create_line(0, y0,
                       canvas_width, y0,
                       fill=color_axes)


def draw_line_perspective():
    draw_fild_z_line()
    draw_fild_x_line()


def draw_fild_z_line():
    global r, n, h
    for i in range(int(-n / 2), int(n / 2)):
        x1 = i
        y1 = h

        for j in range(1, n):
            y = h
            x = i
            z = j
            y2 = y * r / z
            x2 = x * r / z
            canvas.create_line(x1 + x0, y1 + y0,
                               x2 + x0, y2 + y0,
                               fill=color_line)
            x1 = x2
            y1 = y2


def draw_fild_x_line():
    global r, n, h
    for j in range(1, n):
        x1 = j
        y1 = h
        for i in range(int(-n / 2), int(n / 2)):
            y = h
            x = i
            z = j
            y2 = y * r / z
            x2 = x * r / z
            canvas.create_line(x1 + x0, y1 + y0,
                               x2 + x0, y2 + y0,
                               fill=color_line)
            x1 = x2
            y1 = y2


def draw_line_perspective2():
    global r, n, h
    r *= 4
    draw_fild_z_line2()
    draw_fild_x_line2()


def draw_fild_z_line2():
    global r, n, h
    for i in range(int(-n / 2), int(n / 2)):
        x1 = i
        y1 = h
        for j in range(1, n):
            y = h
            x = i
            z = j
            y2 = y * r / z * 1 / ((y ** 2 + z ** 2) ** 0.5)
            x2 = x * r / z * 1 / ((x ** 2 + z ** 2) ** 0.5)
            canvas.create_line(x1 + x0, y1 + y0,
                               x2 + x0, y2 + y0,
                               fill=color_sin)
            x1 = x2
            y1 = y2


def draw_fild_x_line2():
    global r, n, h
    for j in range(1, n):
        x1 = j
        y1 = h
        for i in range(int(-n / 2), int(n / 2)):
            y = h
            x = i
            z = j
            y2 = y * r / z * 1 / ((y ** 2 + z ** 2) ** 0.5)
            x2 = x * r / z * 1 / ((x ** 2 + z ** 2) ** 0.5)
            canvas.create_line(x1 + x0, y1 + y0,
                               x2 + x0, y2 + y0,
                               fill=color_sin)
            x1 = x2
            y1 = y2


def draw_line_perspective3():
    global r, n, h
    r = 4
    draw_fild_z_line3()
    draw_fild_x_line3()


def draw_fild_z_line3():
    global r, n, h
    for i in range(int(-n / 2), int(n / 2)):
        x1 = i
        y1 = h
        for j in range(1, n):
            y = h
            x = i
            z = j
            y2 = r * (y / z + 1 / 2 * (y / z) ** 3 / 3 + 1 / 2 * 3 / 4 * (y / z) ** 5 / 5)
            x2 = r * (x / z + 1 / 2 * (x / z) ** 3 / 3 + 1 / 2 * 3 / 4 * (x / z) ** 5 / 5)
            canvas.create_line(x1 + x0, y1 + y0,
                               x2 + x0, y2 + y0,
                               fill=color_arcsin)
            x1 = x2
            y1 = y2


def draw_fild_x_line3():
    global r, n, h
    for j in range(1, n):
        x1 = j
        y1 = h
        for i in range(int(-n / 2), int(n / 2)):
            y = h
            x = i
            z = j
            y2 = r * (y / z + 1 / 2 * (y / z) ** 3 / 3 + 1 / 2 * 3 / 4 * (y / z) ** 5 / 5)
            x2 = r * (x / z + 1 / 2 * (x / z) ** 3 / 3 + 1 / 2 * 3 / 4 * (x / z) ** 5 / 5)
            canvas.create_line(x1 + x0, y1 + y0,
                               x2 + x0, y2 + y0,
                               fill=color_arcsin)
            x1 = x2
            y1 = y2


if __name__ == '__main__':
    init_canvas()

    radius = 100
    height = 10
    n = 40
    step = 3

    fild = GeometryObject("fild", n, step, height, radius, "line")    #(fild_or_cylinder, row, step, height, radius, line_notLine_notLine2)

    draw_axes()

    mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
