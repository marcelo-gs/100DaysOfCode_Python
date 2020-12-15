# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
result = 0
for letter in two_digit_number:
    try:
        result += int(letter)
    except:
        #avoid an error convertion by a caracter that is not a number
        pass

print(result)


