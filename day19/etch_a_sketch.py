from turtle import Turtle, Screen


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.back(10)


def move_counter_clockwise():
    turtle.right(10)


def move_clockwise():
    turtle.left(10)


def clear():
    turtle.clear()


turtle = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
