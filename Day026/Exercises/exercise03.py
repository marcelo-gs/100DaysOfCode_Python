
# Write your code above 👆
with open("file1.txt") as f_1:
    list_1 = [int(n) for n in f_1.readlines() if n != ""]

with open("file2.txt") as f_2:
    list_2 = [int(n) for n in f_2.readlines() if n != ""]

result = [n for n in list_1 if n in list_2]
#Sorting 
result.sort()
print(result)

