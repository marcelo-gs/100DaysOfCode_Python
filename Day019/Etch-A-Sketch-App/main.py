from turtle import Turtle,Screen, colormode

##MAIN
tom = Turtle()

def move_forwards():
    tom.fd(10)

def move_backwards():
    tom.back(10)

def turn_left():
    tom.seth(tom.heading()-10)

def turn_right():
    tom.seth(tom.heading()+10)

def clearDrawing():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen = Screen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="W", fun=move_forwards)

screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="S", fun=move_backwards)

screen.onkey(key="A", fun=turn_left)
screen.onkey(key="a", fun=turn_left)

screen.onkey(key="D", fun=turn_right)
screen.onkey(key="d", fun=turn_right)

screen.onkey(key="C", fun=clearDrawing)
screen.onkey(key="c", fun=clearDrawing)
screen.listen()
screen.exitonclick()