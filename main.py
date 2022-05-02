# This is a sample Python script.
from math import asin, cos, sin, atan
from math import pi
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
color_sphere = '#37eb34'
color_2atan = BLUE

canvas_height = 800
canvas_width = 800
x0 = canvas_width / 2
y0 = canvas_width * 1 / 3

screen = pygame.display.set_mode((canvas_width, canvas_height))

clock = pygame.time.Clock()


class GeometryObject:
    def __init__(self, field_or_cylinder, row, step, height, diameter, line_notLine_notLine2):
        self.field_or_cylinder = field_or_cylinder
        self.row = row
        self.step = step
        self.height = height
        self.diameter = diameter
        self.line_notLine_notLine2 = line_notLine_notLine2
        self.coordinate_x = [[0] * (self.row + 1) for i in range(2 * (self.row + 1))]
        self.coordinate_y = [[0] * (self.row + 1) for i in range(2 * (self.row + 1))]
        self.coordinate_z = [[0] * (self.row + 1) for i in range(2 * (self.row + 1))]
        self.radius_of_cylinder = self.row * self.step / (2 * pi)

        # make coordinate
        if self.field_or_cylinder == "field":
            self.make_field()
        else:
            self.make_cylinder()

        # make 2d projection and draw it
        if self.line_notLine_notLine2 == "line":
            self.make_2d_line()
        elif self.line_notLine_notLine2 == "notLine":
            self.make_2d_notLine()
        elif self.line_notLine_notLine2 == "sphere":
            self.make_2d_sphere()
        elif self.line_notLine_notLine2 == "2atan":
            self.make_2d_2atan()
        else:
            self.make_2d_notLine2()

        # move the object

    def move_the_object(self, dx, dy):
        self.move_it(dx, dy)
        if self.line_notLine_notLine2 == "line":
            self.make_2d_line()
        elif self.line_notLine_notLine2 == "notLine":
            self.make_2d_notLine()
        elif self.line_notLine_notLine2 == "sphere":
            self.make_2d_sphere()
        elif self.line_notLine_notLine2 == "2atan":
            self.make_2d_2atan()
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
                x1 = self.diameter * asin(x / (z ** 2 + x ** 2) ** 0.5)
                y = self.coordinate_y[k][i]
                y1 = self.diameter * asin(y / (z ** 2 + y ** 2) ** 0.5)
                x2d.append(x1)
                y2d.append(y1)

            if len(x2d) >= 2:
                self.draw_a_line_from_array(x2d, y2d, color)
            x2d = []
            y2d = []

    def make_2d_sphere(self):
        color = color_sphere
        x2d = []
        y2d = []
        for k in range(0, 2 * (self.row + 1)):
            for i in range(0, (self.row + 1)):
                if self.coordinate_z[k][i] <= 0:
                    z = 0.01
                else:
                    z = self.coordinate_z[k][i]
                x = self.coordinate_x[k][i]
                y = self.coordinate_y[k][i]
                l = self.diameter * atan(y / (z ** 2 + x ** 2) ** 0.5)

                x = self.diameter * atan(x / z)
                y = l

                x2d.append(x)
                y2d.append(y)

            if len(x2d) >= 2:
                self.draw_a_line_from_array(x2d, y2d, color)
            x2d = []
            y2d = []

    def make_2d_2atan(self):
        color = color_2atan
        x2d = []
        y2d = []
        for k in range(0, 2 * (self.row + 1)):
            for i in range(0, (self.row + 1)):
                if self.coordinate_z[k][i] <= 0:
                    z = 0.01
                else:
                    z = self.coordinate_z[k][i]
                x = self.coordinate_x[k][i]
                y = self.coordinate_y[k][i]
                l = self.diameter * atan(((x ** 2 + y ** 2) ** 0.5) / z)
                if y != 0:
                    alpha = atan(x / y)
                else:
                    alpha = atan(x / 0.001)

                if y > 0:
                    x = l * sin(alpha)
                    y = l * cos(alpha)
                else:
                    x = -l * sin(alpha)
                    y = -l * cos(alpha)
                x2d.append(x)
                y2d.append(y)

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
            x1, y1 = x2, y2

    def make_cylinder(self):
        k = 0
        # make vertical lines (direction z)
        d_alpha = 2 * pi / self.row
        alpha = 0
        for i in range(0, self.row + 1):
            for j in range(0, self.row + 1):
                x = self.radius_of_cylinder * cos(i * d_alpha)
                y = self.radius_of_cylinder * sin(i * d_alpha) + self.radius_of_cylinder - self.height
                z = j * self.step
                self.coordinate_x[k][j] = x
                self.coordinate_y[k][j] = y
                self.coordinate_z[k][j] = z
            k += 1

        # make horizontal lines (direction x)
        for j in range(0, self.row + 1):
            t = 0
            for i in range(0, self.row + 1):
                x = self.radius_of_cylinder * cos(i * d_alpha)
                y = self.radius_of_cylinder * sin(i * d_alpha) + self.radius_of_cylinder - self.height
                z = j * self.step
                self.coordinate_x[k][t] = x
                self.coordinate_y[k][t] = y
                self.coordinate_z[k][t] = z
                t += 1
            k += 1


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
                    for object_i in group_to_draw:
                        object_i.move_the_object(0, step)
                    draw_axes()
                elif event.key == pygame.K_UP:
                    screen.fill(WHITE)
                    for object_i in group_to_draw:
                        object_i.move_the_object(0, -step)
                    draw_axes()
                elif event.key == pygame.K_LEFT:
                    screen.fill(WHITE)
                    for object_i in group_to_draw:
                        object_i.move_the_object(-step, 0)
                    draw_axes()
                elif event.key == pygame.K_RIGHT:
                    screen.fill(WHITE)
                    for object_i in group_to_draw:
                        object_i.move_the_object(step, 0)
                    draw_axes()

        pygame.display.flip()  # draw all the things
        clock.tick(FPS)  # new iteration


if __name__ == '__main__':
    diameter = canvas_width
    height = 2
    n = 20
    step = 1
    pygame.display.set_caption("Perspective")
    screen.fill(WHITE)

    to_draw = "field"

    if to_draw == "cylinder":
        field_line = GeometryObject(
            "field", n, step, height, diameter, "line")
        field_not_line = GeometryObject(
            "field", n, step, height, diameter, "line")
        field_not_line2 = GeometryObject(
            "field", n, step, height, diameter, "2atan")

        group_of_fields = [field_line, field_not_line, field_not_line2]
        group_to_draw = group_of_fields
    else:
        cylinder_line = GeometryObject(
            "cylinder", n, step, height, diameter, "line")
        cylinder_not_line = GeometryObject(
            "cylinder", n, step, height, diameter, "2atan")
        cylinder_not_line2 = GeometryObject(
            "cylinder", n, step, height, diameter, "line")
        group_of_cylinders = [cylinder_line, cylinder_not_line2, cylinder_not_line]
        group_to_draw = group_of_cylinders

    draw_axes()
    main_loop_start()
