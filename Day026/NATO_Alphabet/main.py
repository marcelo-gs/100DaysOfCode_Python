import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = list(input("What's your word to transform to NATO Alphabet? ").upper())
    try:
        nato_word = [nato_alphabet[letter] for letter in word if letter in nato_alphabet]
    except KeyError:
        print("Sory, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(nato_word)

generate_phonetic()
