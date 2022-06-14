from turtle import Turtle,Screen
import random
screen = Screen()

screen.setup(width=500,height=400)
user_bet=screen.textinput("Which turtle you bet on?","Select a color:")

colors=["orange","red","green","blue","purple","yellow"]
all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=20+(-20*turtle_index))
    all_turtles.append(tim)
is_race_on=False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on=False
            winning_turtle=turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won , the winning turtle is {winning_turtle}")
            else:
                print(f"You've Lost! , the winning turtle is {winning_turtle}")

        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
    
screen.exitonclick()