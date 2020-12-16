# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

div4 = (year % 4) ==0
div100 = (year % 100) ==0
div400 = (year % 400) ==0

leap = False
if div4:
    leap = True
    if div100:
        leap = False
        if div400:
            leap = True

if leap:
    print ("Leap year.")
else:
    print("Not leap year.")