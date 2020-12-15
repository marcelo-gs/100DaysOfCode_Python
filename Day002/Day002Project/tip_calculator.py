#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#1. Create a greeting for your program.
print("Welcome to the Marcelo's Tip calculator")
print("Version 0.1 (Beta Version) - Marcelo Gomes 2020 copyright")
print('')

#2. Total bill
total = input("What was the total bill? $")
try:
    total = float(total)
except:
    totat = 0 

#3. percentage
percentage = input("What percetage tipo would you like to give? 10, 12 or 15? ")
try:
    percentage = float(percentage)
except:
    percentage = 0 

#4. People to split
people = input("How many people to split the bill? ")
try:
    people = int(people)
except:
    people = 0 

result = round((total + ((total * percentage)/100)) / people, 2)
result = "{:.2f}".format(result)
print(f"Each person should pay: ${result}")


"""
Result in Python Console
Code_Python/Day002/Day002Project/tip_calculator.py"
Welcome to the Marcelo's Tip calculator
Version 0.1 (Beta Version) - Marcelo Gomes 2020 copyright

What was the total bill? $124.56
What percetage tipo would you like to give? 10, 12 or 15? 12
How many people to split the bill? 7
Each person should pay: $19.93

*****************************************************
Code_Python/Day002/Day002Project/tip_calculator.py"
Welcome to the Marcelo's Tip calculator
Version 0.1 (Beta Version) - Marcelo Gomes 2020 copyright

What was the total bill? $20
What percetage tipo would you like to give? 10, 12 or 15? 10
How many people to split the bill? 2
Each person should pay: $11.00
"""