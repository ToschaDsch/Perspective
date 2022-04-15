# This is a sample Python script.
import math
import sys
import pygame

# global variable

# there are colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (239, 228, 176)
RED = (255, 0, 0)

FPS = 60  # FPS

color_axes = '#000000'
color_line = '#374534'
color_sin = '#ad1111'
color_arcsin = '#2311ad'

canvas_height = 800
canvas_width = 800
x0 = canvas_width / 2
y0 = canvas_width * 1 / 3

screen = pygame.display.set_mode((canvas_width, canvas_height))

clock = pygame.time.Clock()


class GeometryObject:
    def __init__(self, fild_or_cylinder, row, step, height, diameter, line_notLine_notLine2):
        self.fild_or_cylinder = fild_or_cylinder
        self.row = row
        self.step = step
        self.height = height
        self.diameter = diameter
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

        # move the object

    def move_the_object(self, dx, dy):
        self.move_it(dx, dy)
        if self.line_notLine_notLine2 == "line":
            self.make_2d_line()
        elif self.line_notLine_notLine2 == "notLine":
            self.make_2d_notLine()
        else:
            self.make_2d_notLine2()

    def move_it(self, dx, dy):
        for k in range(0, 2 * (self.row + 1)):
            for i in range(0, (self.row + 1)):
                self.coordinate_x[k][i] += dx
                self.coordinate_z[k][i] += dy

    def make_2d_line(self):
        color = color_line
        x2d = []
        y2d = []
        for k in range(0, 2 * (self.row + 1)):
            for i in range(0, (self.row + 1)):
                if self.coordinate_z[k][i] <= 0:
                    z = 0.01
                else:
                    z = self.coordinate_z[k][i]
                x = self.coordinate_x[k][i] * self.diameter / z
                y = self.coordinate_y[k][i] * self.diameter / z
                x2d.append(x)
                y2d.append(y)

            self.draw_a_line_from_array(x2d, y2d, color)
            x2d = []
            y2d = []

    def make_2d_notLine(self):
        color = color_sin
        x2d = []
        y2d = []
        for k in range(0, 2 * (self.row + 1)):
            for i in range(0, (self.row + 1)):
                if self.coordinate_z[k][i] <= 0:
                    z = 0.01
                else:
                    z = self.coordinate_z[k][i]
                x = self.coordinate_x[k][i]
                x1 = self.diameter * x * z / (z ** 2 + x ** 2)
                y = self.coordinate_y[k][i]
                y1 = self.diameter * y * z / (z ** 2 + y ** 2)
                if abs(y / z) <= 1 and abs(x / z) <= 1:
                    x2d.append(x1)
                    y2d.append(y1)

            if len(x2d) >= 2:
                self.draw_a_line_from_array(x2d, y2d, color)
            x2d = []
            y2d = []

    def make_2d_notLine2(self):
        color = color_arcsin
        x2d = []
        y2d = []
        for k in range(0, 2 * (self.row + 1)):
            for i in range(0, (self.row + 1)):
                if self.coordinate_z[k][i] <= 0:
                    z = 0.01
                else:
                    z = self.coordinate_z[k][i]
                x = self.coordinate_x[k][i]
                x1 = self.diameter * math.asin(x / (z ** 2 + x ** 2)**0.5)
                y = self.coordinate_y[k][i]
                y1 = self.diameter * math.asin(y / (z ** 2 + y ** 2)**0.5)
                #if abs(y / z) <= 1 and abs(x / z) <= 1:
                x2d.append(x1)
                y2d.append(y1)

            if len(x2d) >= 2:
                self.draw_a_line_from_array(x2d, y2d, color)
            x2d = []
            y2d = []

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
    def draw_a_line_from_array(array_x, array_y, color):
        global x0, y0
        x1 = array_x[0]
        y1 = array_y[0]
        for index in range(1, len(array_x)):
            x2 = array_x[index]
            y2 = array_y[index]
            pygame.draw.line(screen, color,
                             (x1 + x0, y1 + y0),
                             (x2 + x0, y2 + y0),
                             )
            x1 = x2
            y1 = y2

    def make_cylinder(self):
        pass


def draw_axes():
    pygame.draw.line(screen, color_axes,
                     (0, y0),
                     (canvas_width, y0), )


def main_loop_start():
    step = 1
    while True:  # the main cycle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    screen.fill(WHITE)
                    fild_line.move_the_object(0, step)
                    fild_not_line.move_the_object(0, step)
                    fild_not_line2.move_the_object(0, step)
                    draw_axes()
                elif event.key == pygame.K_UP:
                    screen.fill(WHITE)
                    fild_line.move_the_object(0, -step)
                    fild_not_line.move_the_object(0, -step)
                    fild_not_line2.move_the_object(0, -step)
                    draw_axes()
                elif event.key == pygame.K_LEFT:
                    screen.fill(WHITE)
                    fild_line.move_the_object(-step, 0)
                    fild_not_line.move_the_object(-step, 0)
                    fild_not_line2.move_the_object(-step, 0)
                    draw_axes()
                elif event.key == pygame.K_RIGHT:
                    screen.fill(WHITE)
                    fild_line.move_the_object(step, 0)
                    fild_not_line.move_the_object(step, 0)
                    fild_not_line2.move_the_object(step, 0)
                    draw_axes()

        pygame.display.flip()  # draw all the things
        clock.tick(FPS)  # neu iteration


if __name__ == '__main__':
    diameter = canvas_width
    height = 2
    n = 100
    step = 1
    pygame.display.set_caption("Perspective")
    screen.fill(WHITE)

    fild_line = GeometryObject(
        "fild", n, step, height, diameter, "line")
    # (fild_or_cylinder, row, step, height, radius, line_notLine_notLine2)
    fild_not_line = GeometryObject(
        "fild", n, step, height, diameter, "notLine")
    # (fild_or_cylinder, row, step, height, radius, line_notLine_notLine2)
    fild_not_line2 = GeometryObject(
        "fild", n, step, height, diameter, "notLine2")
    # (fild_or_cylinder, row, step, height, radius, line_notLine_notLine2)
    draw_axes()
    main_loop_start()
