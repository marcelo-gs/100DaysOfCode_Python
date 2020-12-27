from turtle import Turtle
import random
shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
colors = ['blue', 'green', 'red', 'purple','tan4', 'salmon3', 
        'yellow4','magenta3', 'ivory4', 'BlueViolet', 'DeepPink', 'coral4', 'chocolate2',
        'aquamarine', 'firebrick2', 'orange' ]

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.shape(random.choice(shapes))
        self.color(random.choice(colors))
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)