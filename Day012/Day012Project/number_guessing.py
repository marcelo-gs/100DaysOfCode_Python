###The final project
#No hints

#welcome region

#Choose a difiiculty 
#Easy 10 attempts
#Hard 5 attempts
import random
# import only system from os 
from os import system, name 

##-------
LOGO = """

  _   _                 _                  _____                        _____                      
 | \ | |               | |                / ____|                      / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | | |_ |/ _` | '_ ` _ \ / _ \\
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/  \_____|\__,_|_| |_| |_|\___|
                                                                                                   
                                                                                                   


 
 +-+-+                      
 |B|y|                      
 +-+-+-+-+-+-+-+ +-+-+-+-+-+
 |M|a|r|c|e|l|o| |G|o|m|e|s|
 +-+-+-+-+-+-+-+ +-+-+-+-+-+                                 
                                                            
"""

TOO_HIGH = """
 _____              _     _       _     
/__   \___   ___   | |__ (_) __ _| |__  
  / /\/ _ \ / _ \  | '_ \| |/ _` | '_ \ 
 / / | (_) | (_) | | | | | | (_| | | | |
 \/   \___/ \___/  |_| |_|_|\__, |_| |_|
                            |___/       
"""

TOO_LOW = """

 _____                __               
/__   \___   ___     / /  _____      __
  / /\/ _ \ / _ \   / /  / _ \ \ /\ / /
 / / | (_) | (_) | / /__| (_) \ V  V / 
 \/   \___/ \___/  \____/\___/ \_/\_/  
                                       

"""

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def choice_number():
    """ return a aleatory number between 1 and 100 """
    return random.randint(0, 100) + 1

def attempts(difiiculty):
    """define the number of attempts for each difficulty
        Easy -> 5 attemps
        Hard -> 10 attemps
        Anything else aleatory attemps between 5 and 10"""
    attempts = 0
    if difiiculty == "easy":
        attempts = 10
    elif difiiculty == "hard":
        attempts = 5
    else:
        attempts = random.randint(5, 11)
    return attempts

def make_a_guess(attempts_number):
    print(f"You have {attempts_number} atttempts remaining to guess the number.")
    return int(input("Make a guess: ")), attempts_number-1
    
def check_guess(number, guess):
    if guess > number:
        print(TOO_HIGH)
        return False
    if guess < number:
        print(TOO_LOW)
        return False
    return True

def you_win():
    win_message = """
    
 /$$     /$$ /$$$$$$  /$$   /$$       /$$      /$$ /$$$$$$ /$$   /$$
|  $$   /$$//$$__  $$| $$  | $$      | $$  /$ | $$|_  $$_/| $$$ | $$
 \  $$ /$$/| $$  \ $$| $$  | $$      | $$ /$$$| $$  | $$  | $$$$| $$
  \  $$$$/ | $$  | $$| $$  | $$      | $$/$$ $$ $$  | $$  | $$ $$ $$
   \  $$/  | $$  | $$| $$  | $$      | $$$$_  $$$$  | $$  | $$  $$$$
    | $$   | $$  | $$| $$  | $$      | $$$/ \  $$$  | $$  | $$\  $$$
    | $$   |  $$$$$$/|  $$$$$$/      | $$/   \  $$ /$$$$$$| $$ \  $$
    |__/    \______/  \______/       |__/     \__/|______/|__/  \__/                                                   
    """
    return win_message
def you_lost(number):
    lost_message = """

 /$$     /$$ /$$$$$$  /$$   /$$       /$$        /$$$$$$   /$$$$$$  /$$$$$$$$
|  $$   /$$//$$__  $$| $$  | $$      | $$       /$$__  $$ /$$__  $$|__  $$__/
 \  $$ /$$/| $$  \ $$| $$  | $$      | $$      | $$  \ $$| $$  \__/   | $$   
  \  $$$$/ | $$  | $$| $$  | $$      | $$      | $$  | $$|  $$$$$$    | $$   
   \  $$/  | $$  | $$| $$  | $$      | $$      | $$  | $$ \____  $$   | $$   
    | $$   | $$  | $$| $$  | $$      | $$      | $$  | $$ /$$  \ $$   | $$   
    | $$   |  $$$$$$/|  $$$$$$/      | $$$$$$$$|  $$$$$$/|  $$$$$$/   | $$   
    |__/    \______/  \______/       |________/ \______/  \______/    |__/   

    \n\n
    Corret answer: 
    """ + str(number) + "\n\n"
    return lost_message


end_of_game = False
while not end_of_game:
    clear()
    print(LOGO)
    print("\n\tWelcome to the Number Guessing Game!")
    print("\tI'm thinking of a number between 1 and 100")
    number = choice_number()
    attempts_number = attempts(input("\tChoose a difficulty. Type easy or hard: ").lower())
    number_find = False
    while not number_find:
        again = ""
        guess, attempts_number = make_a_guess(attempts_number)
        if check_guess(number, guess):
            #You Win, you guess the number.
            print(you_win())
            number_find = True
        if attempts_number <=0:
            # you lose!
            number_find = True
            print(you_lost(number))
        if number_find:
            again = input("Do you want to play again? (Y or N)").lower()
            if again =="y" or again == "yes":
                end_of_game = False
            else:
                end_of_game = True
                        
