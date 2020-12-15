# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
try:
    age = int(age)
except:
    age = 0 

age = 90 - age
if age > 0:
    days = age * 365
    weeks = age * 52
    months = age * 12
    print(f"You have {days} days, {weeks} weeks, and {months} months left.")
else:
    print(f"You already have 90 years old")