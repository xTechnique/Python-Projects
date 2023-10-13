import random
import Hangman_art
import Hangman_words

end_of_game = False
chosen_word = random.choice(Hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
print(Hangman_art.logo)
#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter lil onion: ").lower()

    if guess in display:
        print(f"Already guessed {guess}!")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(Hangman_art.stages[lives])
        print(f"Lives left: {lives}")
        print(f'Wrong guesses: {guess}')
        if lives == 0:
            end_of_game = True
            print("You lose")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")