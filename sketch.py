from turtle import Screen , Turtle

turtle= Turtle()

screen = Screen()

screen.listen()

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def move_right():
    turtle.right(10)
def move_left():
    turtle.left(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(move_right,"d")
screen.onkey(move_left,"a")
screen.onkey(clear,"c")

screen.exitonclick()