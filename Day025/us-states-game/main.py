import turtle 
import pandas
ALIGMENT = 'left'
FONT = ('Courier', 8, 'normal')

data = pandas.read_csv("50_states.csv")
states = dict(zip(data["state"].to_list(), zip(data['x'].to_list(), data['y'].to_list())))

#def get_mouse_click_coor(x, y):
#    print(x,y)

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tom = turtle.Turtle() 
tom.hideturtle()
tom.penup()

def print_state(state, coor):
    tom.goto(coor)
    tom.write(state,False, align=ALIGMENT, font=FONT)

#turtle.onscreenclick(get_mouse_click_coor)

game_is_on = True
score = 0

while game_is_on:
    answer = screen.textinput(title=f"Guess the State {score}/50", 
                             prompt="What's another state's name?").title()
    if answer == "Exit":
        game_is_on = False
    if answer in states.keys():
        print_state(answer, states[answer])
        score += 1
    else:
        print(answer)
    if score == 50:
        game_is_on = False


turtle.mainloop()
