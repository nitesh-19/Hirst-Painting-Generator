import turtle
from turtle import Turtle, Screen
from random import randint
import colorgram



class Generator:

    def __init__(self):
        self.tim = None

    def go_up(self, angle, step):
        self.tim.left(angle)
        self.tim.forward(step)
        self.tim.left(angle)

    def extract_color_palette(self, path, number_of_colors):
        colors = colorgram.extract(path, number_of_colors)

        list_of_rgb = []
        for index in range(number_of_colors):
            list_of_rgb.append(tuple(colors[index].rgb))
        return list_of_rgb

    def generate_painting(self, list_of_rgb=None):
        if list_of_rgb is None:
            list_of_rgb = [
                (237, 244, 239), (238, 241, 246), (218, 147, 85), (220, 78, 58), (44, 93, 146),
                (232, 219, 91), (215, 65, 84), (23, 28, 41), (149, 65, 95), (40, 20, 15), (42, 23, 30), (114, 168, 200),
                (147, 69, 59), (196, 136, 159), (32, 133, 92), (73, 166, 93), (121, 182, 139), (236, 221, 9),
                (231, 168, 182),
                (161, 180, 50), (97, 44, 70), (26, 169, 203), (18, 40, 28), (56, 55, 99), (107, 44, 39),
                (234, 172, 160),
                (165, 210, 190), (151, 209, 221)]

        dots_in_x = 14
        dots_in_y = 8
        step = 70
        distance_in_x = dots_in_x * step
        distance_in_y = dots_in_y * step

        angle = -90
        turtle.colormode(255)
        self.tim = Turtle()

        screen = Screen()
        self.tim.penup()
        self.tim.hideturtle()
        self.tim.speed(1000)
        self.tim.setx(-458)
        self.tim.sety(-300)

        for y in range(1, distance_in_y, step):
            rgb_index = randint(0, len(list_of_rgb) - 1)
            angle *= -1
            self.tim.dot(30, tuple(list_of_rgb[rgb_index]))
            for x in range(1, distance_in_x - step, step):
                rgb_index = randint(0, len(list_of_rgb) - 1)
                self.tim.forward(step)
                self.tim.dot(30, tuple(list_of_rgb[rgb_index]))
            self.go_up(angle=angle, step=step)
        ts = turtle.getscreen()
        self.tim.hideturtle()

        ts.getcanvas().postscript(file="output.eps")

        screen.exitonclick()
