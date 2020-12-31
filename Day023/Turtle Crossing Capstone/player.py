from time import sleep
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__(shape="turtle")
        self.penup()
        self.color("black")
        self.seth(90)
        self.go_to_start()

    def up(self):
        self.fd(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def end_of_stage(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False
