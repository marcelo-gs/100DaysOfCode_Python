import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

word = list(input("What's your word to transform to NATO Alphabet? ").upper())
nato_word = [nato_alphabet[letter] for letter in word if letter in nato_alphabet]
print(nato_word)
