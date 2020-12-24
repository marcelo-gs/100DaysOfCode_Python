from turtle import Turtle,Screen, colormode
import random 

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), 
              (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), 
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), 
              (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), 
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), 
              (176, 192, 208), (168, 99, 102)]

tom = Turtle()
tom.color('white')
colormode(255)
tom.penup()
tom.hideturtle()
#tom.pensize(20)
tom.speed(0)
tom.setpos((-200,-200))

def print_dot():
    #tom.color(random.choice(color_list))
    #tom.pendown()
    #tom.forward(1)
    #tom.penup()
    tom.dot(20, random.choice(color_list))
    tom.forward(50)


for _ in range(10):
    tp = tom.pos()
    for _ in range(10):
        print_dot()
    new_pos = (tp[0], tp[1] + 50)
    tom.setpos(new_pos)

tom.color('white')
screen = Screen()
screen.exitonclick()