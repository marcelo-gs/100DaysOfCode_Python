# import only system from os 
from os import system, name 

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

logo = '''
A u c t i o n   P r o g r a m 
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

clear()
end_of_program = False
bids_dict = {}
def personal_bid():
    global bids_dict
    print(logo)
    name = input("What's your name? ")
    bid = float(input("What's your bid? $"))
    bids_dict[name] = bid

def define_who_wins():
    global bids_dict
    clear()
    print(logo)
    max_bid = 0
    winner = ""
    for key in bids_dict:
        if bids_dict[key] > max_bid:
            winner = key
            max_bid = bids_dict[key]
    
    print(f"The highest bid was ${max_bid} and was done by {winner}")


while not end_of_program:
    personal_bid()
    again = input("Are There another bidders? (yes or no) ")
    if again == "no":
        define_who_wins()
        end_of_program = True
    elif again == "yes":
        clear()
    else:
        print("Ester egg !!!\n Program will be closed now!")
        break
    


