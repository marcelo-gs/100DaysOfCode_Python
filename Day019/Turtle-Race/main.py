from turtle import Turtle, Screen, color
import random
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
    
possible_colors = """
🟥 red 
🟧 orange 
🟨 yellow
🟩 green
🟦 blue 
🟪 purple 
"""
user_bet = screen.textinput(title="Make your bet", 
    prompt=f"Which turtle will win the race? \nPoissible colors rainbow 🌈 \n{possible_colors}\nEnter a color: ")



turtles = []
turtle_index = -70
for color in colors:
    turtles.append(Turtle(shape="turtle"))
    turtles[-1].penup()
    turtles[-1].goto(x=-230, y=turtle_index)
    turtles[-1].color(color)
    turtle_index += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                message = "You won"
            else:
                message = "You lost!"
            message += f" The {winning_color} is the winner!"
            print(message)
            is_race_on = False
        turtle.fd(random.randint(1,10))



screen.exitonclick()