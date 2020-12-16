#Write your code below this row 👇

total = 0
for number in range(1, 101):
    aux = ""
    if number % 3 == 0:
       aux += "Fizz"
    if number % 5 == 0:
        aux += "Buzz"
    if aux == "":
        aux = str(number)
    print(aux)
