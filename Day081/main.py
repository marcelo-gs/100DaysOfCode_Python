
ALLOWED_CHAR = {
    "A": "· − ", 
    "B": "− · · · ", 
    'C': "− · − · ", 
    "D": "− · · ", 
    "E": "· ", 
    "F": "· · − · ", 
    "G": "− − · ", 
    "H": "· · · · ",
    "I": "· · ",
    "J": "· − − − ", 
    "K": "− · − ", 
    "L": "· − · · ",
    "M": "− −",
    "N": "− · ",
    "O": "− − −", 
    "P": "· − − ·", 
    "Q": "− − · − ", 
    "R": "· − · ", 
    "S": "· · · ", 
    "T": "− ", 
    "U": "· · −", 
    "V": "· · · − ", 
    "W": "· − − ", 
    "X": "− · · − ", 
    "Y": "− · − − ", 
    "Z": "− − · · ", 
    "0": "− − − − − ", 
    "1": "· − − − − ", 
    "2": "· · − − − ", 
    "3": "· · · − − ", 
    "4": "· · · · − ", 
    "5": "· · · · · ", 
    "6": "− · · · · ", 
    "7": "− − · · · ", 
    "8": "− − − · · ", 
    "9": "− − − − · ",
    ".": "· − · − · − ",
    ",": "− − · · − − ",
    "?": "· · − − · · ",
    "'": "· − − − − · ",
    "!": "− · − · − − ",
    "+": "· − · − · ",
    "-": "− · · · · − ",
    "Starting Signal": "− · − · − ",  
    "New Page Signal": "· − · − · ", 
    "End of work" : "· · · − · − ",
    "Error" : "· · · · · · · · "
}

final_message = []
skipped_letters = []

message = ""
while (message != "<exit>"):
    try:
        message = input("Please, Type your message: (Type <exit> to finish)\n").strip().upper()
        if message != "<EXIT>":  
            final_message = []
            skipped_letters = []
            final_message.append(ALLOWED_CHAR["Starting Signal"])
            for letter in message:
                if letter in ALLOWED_CHAR:
                    if letter == "\n":
                        final_message.append(ALLOWED_CHAR["New Page Signal"])
                    else:
                        final_message.append(ALLOWED_CHAR[letter])
                else:
                    skipped_letters.append(letter)
            final_message.append(ALLOWED_CHAR["End of work"])
            if len(final_message) == 2:
                print('No letters to transalate to morse code!')
            else:
                print(f'\n\tMorse Code:\n{" ".join(final_message)}')
    except:
        print(ALLOWED_CHAR["Error"])

