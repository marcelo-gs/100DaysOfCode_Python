# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height ** 2))

response = f"Your BMI is {bmi}, "
if bmi <=18.5:
    response += "you are underweight."
elif bmi <25:
    response += "you have a normal weight."
elif bmi <30:
    response += "you are slightly overweight."
elif bmi <35:
    response += "you are obese."
else:
    response += "you are clinically obese."

print(response)