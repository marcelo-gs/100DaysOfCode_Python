rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

player_choise = input("Please choose Rock(1), Paper(2) or Scissors(3)\n ")

if int(player_choise) not in [1, 2, 3]:
    print("Sorry, Here we play only with Rock, Paper and Scissors")
    exit()

computer_choise = random.randint(0,2)
print(computer_choise)
#define who wins!
"""
Pespective of the player
Computer(rows)/Player(columns)
        Rock        Paper       Scissors
Rock      E           W             L
Paper     L           E             W
Scissors  L           W             E
"""
possibilities = [rock, paper, scissors]

decision_matrix = [["E", "W", "L"], ["L", "E", "W"], ["L", "W", "E"]]

print("Player:")
print(possibilities[int(player_choise)-1])
print("Computer:")
print(possibilities[computer_choise])
if decision_matrix[computer_choise][int(player_choise)-1] == "W":
    print("You Win!")
elif decision_matrix[computer_choise][int(player_choise)-1] == "E":
    print("No one Wins!")
else:
    print("Sorry, you loose!")
