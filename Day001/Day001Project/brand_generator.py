#1. Create a greeting for your program.
print("Welcome to the Marcelo's Brand Generator")
print("Version 0.1 (Beta Version) - Marcelo Gomes 2020 copyright")
print('')

#2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew up?\n").strip() #strip function remove blank spaces on strings

#3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n").strip() #strip function remove blank spaces on strings

#4. Combine the name of their city and pet and show them their band name.
print("Your brand could be '"+ city + ' ' + pet + "'")
