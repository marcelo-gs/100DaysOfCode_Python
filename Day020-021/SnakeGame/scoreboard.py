from turtle import Turtle

ALIGMENT = 'center'
FONT = ('Courier', 15, 'normal')

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        with open("data.snake") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        self.refresh()

    def addScore(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align=ALIGMENT, font=FONT)
        self.reset()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.snake",'w') as data:
                data.write(f"{self.high_score}")
            self.score = 0

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGMENT, font=FONT)