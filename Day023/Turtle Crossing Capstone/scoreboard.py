from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.level = 0
        self.car_speed = 4
        self.cycle = 8
        self.refresh()


    def game_over(self):
        self.goto(0,0)
        font = ("Courier", 24, "bold")
        self.write(arg="G A M E  O V E R", move=False, align=ALIGMENT, font=font)

    def refresh(self):
        self.clear()
        self.write(arg=f"Level {self.level}", move=False, align=ALIGMENT, font=FONT)

    def addLevel(self):
        self.level += 1
        if self.car_speed < 10:
            self.car_speed += 1
        else:
            self.cycle -= 1
            self.car_speed = 6
        self.refresh()

    