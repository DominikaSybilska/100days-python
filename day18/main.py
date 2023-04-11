import random
import turtle as t
import colorgram

COLOR_LIST = [(235, 241, 246), (1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39),
              (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104),
              (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85),
              (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]


def get_color_from_jpg():
    colors = colorgram.extract('dots.jpg', 30)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_tuple = (r, g, b)
        rgb_colors.append(color_tuple)


def draw_dots():
    turtle = t.Turtle()
    screen = t.Screen()
    t.colormode(255)
    turtle.speed(10)
    turtle.pu()
    turtle.hideturtle()
    turtle.setposition(-200, -200)
    number_of_dots = 100
    for dot_count in range(1, number_of_dots + 1):
        turtle.dot(20, random.choice(COLOR_LIST))
        turtle.forward(50)
        if dot_count % 10 == 0:
            turtle.left(90)
            turtle.forward(50)
            turtle.setheading(180)
            turtle.forward(500)
            turtle.setheading(0)

    screen.exitonclick()


if __name__ == '__main__':
    draw_dots()
