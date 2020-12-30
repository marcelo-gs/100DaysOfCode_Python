import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score = ScoreBoard()
screen.onkey(player.up, "Up")


game_is_on = True
cycle = 0
while game_is_on:
    cycle += 1 
    time.sleep(0.1)
    screen.update()
    if cycle % score.cycle == 0:
        car_manager.create_car()
    car_manager.move()
    if car_manager.collision(player):
        game_is_on = False
        score.game_over()
    if player.end_of_stage():
        score.addLevel()
        player.go_to_start()
        car_manager.change_speed()
        
screen.exitonclick()
