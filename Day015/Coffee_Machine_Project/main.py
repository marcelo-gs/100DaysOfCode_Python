from data import MENU, resources
from os import system, name 

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def coffee_types():
    items = ""
    for key in MENU:
        items += key + "/"
    items = items[:-1]
    return items

def check_resources(type_of_coffee, coffee_resources):
    """Check if has enough water, milk and coffee in resources
        return True or False and the resource that was not enough """
    resources_enough = True
    message = ""
    ingredients = MENU[type_of_coffee]['ingredients']
    for item in ingredients:
        if ingredients[item] > coffee_resources[item]:
            return False, item

    return True, str

def check_transaction(type_of_coffee, coffee_resources):
    cost = MENU[type_of_coffee]['cost']
    return cost <= coffee_resources['transaction']

def reset_machine(resources):
    coffee_resource = {}
    coffee_resource = resources.copy()
    coffee_resource["money"] = 0
    coffee_resource['transaction'] = 0
    for coffee in coffee_types().split('/'):
        coffee_resource[coffee] = 0
    return coffee_resource

def calc_coins(pennies, nickles, dimes, quaters):
    total_fund = 0 
    total_fund += (pennies * 0.01)
    total_fund += (nickles * 0.05)
    total_fund += (dimes * 0.1)
    total_fund += (quaters * 0.25)
    return total_fund

def insert_money():
    print("Accepted coins:\n\tPennies($0.01)\n\tNickles($0.05)\n\tDimes($0.1)\n\tQuaters($0.25)\n")
    total_fund = 0
    while True:
       pennies = int(input("How many pennies: "))
       nickles = int(input("How many nickles: "))
       dimes = int(input("How many dimes: "))
       quaters = int(input("How many quaters: "))
       total_fund += calc_coins(pennies, nickles, dimes, quaters)
       print(f"\nYou input ${total_fund}\n")
       if input("Would you like to add more coins? (Y or N) ").upper() == "N":
           coffee_resources['transaction'] = total_fund
           return 
def use_resources(type_of_coffee):
    ingredients = MENU[type_of_coffee]['ingredients']
    for item in ingredients:
        coffee_resources[item] -= ingredients[item]
    return

def confirm_transaction(type_of_coffee):
    cost = MENU[type_of_coffee]['cost']
    coffee_resources['transaction'] -= cost
    coffee_resources['money'] += cost
    coffee_resources[type_of_coffee] += 1
    return

def print_report(coffee_resources):
    print(f"Walter: {coffee_resources['water']}ml")
    print(f"Milk: {coffee_resources['milk']}ml")
    print(f"Coffee: {coffee_resources['coffee']}g")
    print(f"Money: ${coffee_resources['money']}")
    for coffee in coffee_types().split("/"):
        print(f"\t{coffee}: {coffee_resources[coffee]}")
    input("\nType <enter> to return...")

def making_coffee(type_of_coffee):
    clear()
    use_resources(type_of_coffee)
    confirm_transaction(type_of_coffee)
    print(f"Here is your {type_of_coffee}. Enjoy!")
    input("\nType <enter> to return...")

def refuel_machine():
    print(f"Accepted resources:\n\tWater {coffee_resources['water']}(ml)\n\tMilk {coffee_resources['milk']}(ml)\n\tCoffee {coffee_resources['coffee']}(g)\n")
    coffee_resources['water'] += int(input("How much water (ml): "))
    coffee_resources['milk'] += int(input("How much milk (ml): "))
    coffee_resources['coffee'] += int(input("How much coffee (g): "))
    print_report(coffee_resources)

def print_help():
    clear()
    print("Welcome to help page")
    print("\nPossible commands:")
    print("\t\t off --> Turn off Coffee machine")
    print("\t\t report --> Print a report of the resources")
    print("\t\t reset --> Reset machine for original setting")
    print("\t\t refuel --> Refuel resources (walter, milk and coffee")
    input("\nType <enter> to return...")

#TODO: Machine On....
print("Coffee Machine is On")
coffee_resources = reset_machine(resources)
machine_on = True

while machine_on:
    clear()
    choice = input("\nWhat would you like? (" + coffee_types()+")").lower().strip()
    if choice == "off":
        machine_on = False
        print_report(coffee_resources)
        print("Turning off Coffee Machine")
    elif choice == "report":
        #print(coffee_resources)
        print_report(coffee_resources)
    elif choice == "reset": #######################
        coffee_resources = reset_machine(resources)
        print("Resources fulfilmented")
    elif choice == "refuel":
        refuel_machine()
    elif choice == "help":
        print_help()
    else:
        resources_enough = False
        message = ""
        resources_enough, message  = check_resources(choice, coffee_resources)
        if resources_enough:
            insert_money()
            if check_transaction(choice, coffee_resources):
                making_coffee(choice)
                if coffee_resources['transaction'] > 0:
                    print(f"Here is ${coffee_resources['transaction']} dollars in change.")
                    coffee_resources['transaction'] = 0
                    input("\nType <enter> to return...")

            else:
                print("Sorry that's not enough money. Money refunded.")
                coffee_resources['transaction'] = 0
                input("\nType <enter> to return...")

            
        else:
            print(f"Sorry there is not enough {message}")
            input("\nType <enter> to return...")

