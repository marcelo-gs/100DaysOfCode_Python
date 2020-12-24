##Turtle Project
from turtle import Turtle,Screen, colormode,clear
import random 

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


tom = Turtle()
tom.color('blue', 'yellow')

colormode(255)
tom.speed(0)

def draw_spirograth(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)

for number in range(15, 4, -1):
    clear()
    draw_spirograth(number)
screen = Screen()
screen.exitonclick()