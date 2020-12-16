name1 = input("What is your name?\n").upper()
name2 = input("What is their name?\n").upper()

count1 = 0 
count2 = 0 

count1 += name1.count("T")
count1 += name1.count("R")
count1 += name1.count("U")
count1 += name1.count("E")

count1 += name2.count("T")
count1 += name2.count("R")
count1 += name2.count("U")
count1 += name2.count("E")

count2 += name1.count("L")
count2 += name1.count("O")
count2 += name1.count("V")
count2 += name1.count("E")

count2 += name2.count("L")
count2 += name2.count("O")
count2 += name2.count("V")
count2 += name2.count("E")

total = int(str(count1) + str(count2))

if total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
elif total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
else:
    print(f"Your score is {total}.")