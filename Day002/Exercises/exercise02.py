# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
try:
    height = float(height)
    weight = float(weight)
except:
    #this just avoid error convertion 
    height = 0 
    weight = 0 

bmi = int(weight / (height**2))

print(bmi)
