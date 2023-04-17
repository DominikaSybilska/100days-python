import random
from turtle import Turtle, Screen

is_race_on = False
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
screen = Screen()
screen.setup(width=500, height=400)

if __name__ == '__main__':
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    y_coordinate = -100
    for i in range(0, 6):
        turtle = Turtle(shape="turtle")
        turtle.pu()
        turtle.color(COLORS[i])
        turtle.goto(x=-230, y=y_coordinate)
        y_coordinate += 30
        turtles.append(turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:

        for one_turtle in turtles:
            if one_turtle.xcor() > 230:
                is_race_on = False
                winning_color = one_turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is winner.")
                else:
                    print(f"You've lost. The {winning_color} turtle is winner.")


            random_distance = random.randint(0, 10)
            one_turtle.forward(random_distance)

    screen.exitonclick()
