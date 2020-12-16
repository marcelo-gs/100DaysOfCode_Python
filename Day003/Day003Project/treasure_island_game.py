print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("\n\n\n\n")
print("You are in an Island and you have 2 ways to go")
win = False
left_right = input("What side do you choose? (left or right)\n").lower()
if left_right == "left":
    print("You walk for 1 minute and find a river")
    print("You can swin to cross the river or wait for a boat to cross")
    swin_wait = input("What do you choose? (swim or wait)\n").lower()
    if swin_wait == "wait":
        print("Good...Good. Your boat arrived and you cross the river.")
        print("After walking for 2 minutes, you find 3 doors.")
        print("Each door has a color")
        print("One is Red")
        print("The other is Yellow")
        print("And the last one is Blue")
        colors = input("What color do you choose? (red, yellow or blue)\n").lower()
        if colors =="yellow":
            print("You should pass!!!")
            print("You find the treasure and win the game.")
        elif colors == "blue":
            print("Great choose. When you open blue the door you find beasts.\nYou was eaten by beasts.")
            print("Game Over. Please Try again")
        elif colors == "red":
            print("Nice choose. When you open red the door you find fire.\nYou burned by fire.")
            print("Game Over. Please Try again")
        else:
            print(f"Wrong color. There is not door with this color: {colors}\nGame Over.Please Try again")
    else:
        print("You are brave!!! You choose to swim.")
        print("But..., sorry you was attacked by trout")
        print("Game Over. Please Try again")

else:
    print("You walk for 2 minutes")
    print("But, sorry. You fall into a hole.")
    print("Game Over. Please Try again")