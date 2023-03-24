import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)

lives = 6
display = []
end_of_game = False

print(hangman_art.logo)

for letter in chosen_word:
    display.append("_")
print(display)

while not end_of_game:
    guess = input("Guess a letter ").lower()
    i = 0

    if guess in display:
        print("You have already entered this letter.")

    for letter in chosen_word:
        if letter == guess:
            display[i] = letter
        i += 1
    if guess not in chosen_word:
        print("This letter doesn't appear in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
