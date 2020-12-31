#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("../Day024/Mail Merge Project/Input/Letters/starting_letter.docx") as f_letter:
    model  = f_letter.read()

lines = []
with open('../Day024/Mail Merge Project/Input/Names/invited_names.txt') as f_names:
    for name in f_names.readlines():
        f = open(f'../Day024/Mail Merge Project/Output/ReadyToSend/{name.strip()}.docx', mode="w")
        f.write(model.replace("[name]", name.strip()))
        f.close()
