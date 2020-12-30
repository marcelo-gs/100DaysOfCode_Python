from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.cars =[]
        self.car_speed = STARTING_MOVE_DISTANCE
        

    def create_car(self):
        car = Turtle("square")
        car.turtlesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.speed(4)
        car.goto((300,random.randint(-245,245)))

        self.cars.append(car)
    

    def move(self):
        for car in self.cars:
            car.back(self.car_speed)

    def change_speed(self):
        self.car_speed += MOVE_INCREMENT

    def collision(self, turtle):
        for car in self.cars:
            if car.distance(turtle) < 20:
                return True
        return False