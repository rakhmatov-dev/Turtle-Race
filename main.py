import random
from turtle import Turtle, Screen

color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

x_start = -230
x_finish = 230
y_start = -70
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color from a rainbow: ")
all_turtles = []

random.shuffle(color_list)
for n in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("slow")
    new_turtle.color(color_list[n])
    new_turtle.penup()
    new_turtle.goto(x=x_start, y=y_start + (n + 1) * 30)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    random.shuffle(all_turtles)
    for turtle in all_turtles:
        pace = random.randint(0, 10)
        turtle.forward(pace)
        if turtle.xcor() >= x_finish:
            is_race_on = False
            break

if turtle.pencolor() == user_bet.lower():
    print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
else:
    print(f"You've lost! The {turtle.pencolor()} turtle is the winner!")

screen.exitonclick()