from game_data import data
from art import logo, vs
import random
from os import system, name 


used_data = []
score = 0 


def start_game():
    clear()
    print(logo)
    return False


def get_aleatory_info():
    find = False
    position = 0
    while not find:
        position = random.randint(0,len(data)-1)
        name = data[position]["name"]
        if name not in used_data:
            used_data.append(name)
            find = True
            return data[position]


def print_dispute(dataA, dataB):
    print(f"Compare A: {dataA['name']}, {dataA['description']} from {dataA['country']}")
    print(vs)
    print(f"Against B: {dataB['name']}, {dataB['description']} from {dataB['country']}")


def who_wins(dataA, dataB):
    if int(dataA['follower_count']) > int(dataB['follower_count']):
        return "A"
    else:
        return "B"


# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


data_A = get_aleatory_info()
data_B = get_aleatory_info()

end_of_game = start_game()
while not end_of_game:
    print_dispute(data_A, data_B)
    answer = input("\nWho has more followers (Type 'A' or 'B'): ").upper()
    if answer == who_wins(data_A, data_B):
        print("Win")
        if answer == "B":
            data_A = data_B
        end_of_game = start_game()
        data_B = get_aleatory_info()
        score += 1
        print(f"You're right! Current score: {score}")
        
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        end_of_game = True
