############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

#I only use Hint 1 and 2: 😭 hahhaa
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = []
def reset_cards():
    global cards
    cards = ["A♥️", "2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️", "K♥️"]
    cards.extend(["A♦️", "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️"])
    cards.extend(["A♣️", "2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️", "8♣️", "9♣️", "10♣️", "J♣️", "Q♣️", "K♣️"])
    cards.extend(["A♠️", "2♠️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️"])
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the dyeck as they are drawn.
## The computer is the dealer.

## Import area
import random
from os import system, name 

####### Functions

# define our clear function 
def clear(): 
    """ Clear terminal for best results.
        works on Windows, Mac and Linux """
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# Define a function to return a aleatory card 
def choice_card():
    global cards
    card = random.choice(cards)
    cards.remove(card)
    return card

def remove_symbol(card):
    """remove symbol to calculate score
    accepted symbols ♥️ ♦️ ♣️ ♠️
    """
    return card.replace("♥️", "").replace("♦️", "").replace("♣️", "").replace("♠️", "")

# function to calc Score
def cal_score(player):
    count = 0
    blackjack = False
    hand = []
    for card in player["cards"]:
        card = remove_symbol(card)
        hand.append(card)
        
    if len(hand) == 2:
        for card in hand:
            if card in ("J", "Q", "K"):
                blackjack = True
        if "A" in hand and blackjack:          
            blackjack = True
        else:
            blackjack = False
    for card in hand:
        if card in ("J", "Q", "K"):
            card = 10
        if card == "A":
            card = 11
        count += int(card)
    if blackjack:
        count = 21
    if count > 21:
        for card in hand:
            if card == "A":
                count -= 10
    return count
    

def print_hand(hand, type):
    if type == "player":
        print(f"\tYour cards: {hand['cards']} current score {hand['Score']}")
    else:
        print(f"\tComputer's first card: {hand['cards'][0]}")

def inicial_question():
    clear()
    print(logo)
    return input("Do you want to play a game of Blackjack?\nType y(yes) or n(no)\n ->").lower()

def print_final_hand():
    global player
    global computer
    clear()
    print(f"\tYour final hand: {player['cards']} final score: {player['Score']}")
    print(f"\tComputer's final card: {computer['cards']} final score: {computer['Score']}")

def dealer_choise():
    global computer
    #Dealer works with security numbers! hahaha
    while computer["Score"] < 18:
        computer["cards"].append(choice_card())
        computer["Score"] = cal_score(computer)

def new_game():
    global player
    global computer
    player = {
    "cards":list(), 
    "Score": 0, 
    }
    computer = {
    "cards":list(), 
    "Score": 0, 
    }
    if inicial_question() == "y":
        reset_cards()
        player["cards"].append(choice_card())
        player["cards"].append(choice_card())
        player["Score"] = cal_score(player)
        computer["cards"].append(choice_card())
        computer["cards"].append(choice_card())
        computer["Score"] = cal_score(computer)
        print_hand(player, "player")
        print_hand(computer, "computer")
        return False
    else:
        return True
#Variables
logo = """
Marcelo Gomes's version of:\n
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   



###main program.. Starts here
end_game = new_game()
while not end_game:
    another_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
    if another_card == "y":
        player["cards"].append(choice_card()) 
        player["Score"] = cal_score(player)
        print_hand(player, "player")
        print_hand(computer, "computer")
        if player["Score"] > 21:
            end_game = True
            #By the rules I really think call dealer_choise() is not necessary!
            #dealer_choise()
            print_final_hand()
            print("You went over. You lose 😭")
            input("\n\nPress <enter>") 
            end_game = new_game()
    else:
        dealer_choise()
        print_final_hand()
        if player["Score"] == computer["Score"]:
            print("\n\tWithdraw!!!")
            print("\tNo one wins")
        elif player["Score"] == 21 or player["Score"] > computer["Score"]:
            print("\n\t Y o u   W i n !")
        if computer["Score"] > 21 and player["Score"] < 21:
            print("\n\t Y o u   W i n !")
        else:
            ##Rule:
            #If both the dealer and player bust, the player loses. **bust = exceed 21
            print("\n\tDealer Win!")

        input("\n\nPress <enter>") 
        end_game = new_game()
    #end_game = True


##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.
