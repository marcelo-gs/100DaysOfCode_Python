import random
from systemClear import clear
from hangman_lib import logo,word_list, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guessed = []

print(logo)


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess not in guessed:    
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            #print(f"Current position: {position}\n Current letter: "{letter}"\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:
            #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(f"You wrong your guess. This lettter '{guess}' not exist in the word.")
            guessed.append(guess)
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose. The chosen word was " + "".join(chosen_word))

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
    
    else:

        print(f"This letter '{guess}' already was guessed")

    #TODO-2: - Import the stages from hangman_lib.py and make this error go away.
    print(stages[lives])