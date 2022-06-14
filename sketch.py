from turtle import Screen , Turtle

tim= Turtle()

screen = Screen()

screen.listen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_right():
    tim.right(10)
def move_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(move_right,"d")
screen.onkey(move_left,"a")
screen.onkey(clear,"c")

screen.exitonclick()