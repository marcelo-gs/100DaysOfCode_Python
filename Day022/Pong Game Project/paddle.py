from turtle import Turtle
WIDTH = 20
HEIGHT = 100
STARTING_POSITIONS = {"Left":(-350,0), "Right": (350,0)}
class Paddle(Turtle):

    def __init__(self, position="Right") -> None:
        super().__init__(shape="square")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(STARTING_POSITIONS[position])
        self.speed(10)
    
    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)
