import random

player_lives = 0
end_game = False


def set_difficulty(set_level):
    if set_level == 'easy':
        return player_lives + 10
    elif set_level == 'hard':
        return player_lives + 5


def number():
    random_int = random.randint(1, 100)
    return random_int


def compare_number(comp_num, player_num):
    if comp_num > player_num:
        print("Too low.\nGuess again.")
    elif player_num > comp_num:
        print("Too high\nGuess again.")
    elif player_num == comp_num:
        return 0


if __name__ == '__main__':
    print("Welcome to the Number Guessing Game!\nI'm thinking the number between 1 and 100.")
    difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")
    level = set_difficulty(difficulty)
    computers_number = number()
    print(f"You have {level} attempt remaining to guess the number. ")
    while not end_game:
        guess_number = int(input('Make a guess: '))
        result = compare_number(computers_number, guess_number)
        if result == 0:
            end_game = True
            print(f"You got it! The answer was {computers_number}")
        else:
            level -= 1
            if level == 0:
                print("You've run out of guesses, you lose.")
                end_game = True
            else:
                print(f"You have {level} attempt remaining to guess the number. ")

