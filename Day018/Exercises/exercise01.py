##Turtle Project
from turtle import Turtle,Screen, colormode
import random 

colors=['blue', 'green', 'black', 'red', 'purple','tan4', 'salmon3', 
        'yellow4','magenta3', 'ivory4', 'BlueViolet', 'DeepPink', 'coral4', 'chocolate2',
        'aquamarine', 'firebrick2', 'orange' ]

directions = [0,90,180,270]
#timmy = Turtle()
#timmy.shape('turtle')
#timmy.color('red', 'green')
tom = Turtle()
tom.shape('turtle')
tom.color('blue', 'yellow')

def draw_object(side):
    tom.color(random.choice(colors))
    angle = 360/side
    for _ in range(side):
        tom.fd(100)
        tom.right(angle)

#for side in range(3,20):
    draw_object(side)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

colormode(255)
tom.pensize(15)
tom.speed('fastest')
def random_walk(turtle):
    turtle.color(random_color())
    turtle.setheading(random.choice(directions))
    turtle.fd(50)

for _ in range(50):
    random_walk(tom)

screen = Screen()
screen.exitonclick()