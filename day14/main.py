import random
import art
from game_data import data

PLAYER_SCORE = 0
IS_GAME_FINISHED = False


def get_account():
    return random.choice(data)


def format_data(account):
    name = account['name']
    desc = account['description']
    country = account['country']
    return f'{name}, a {desc}, from {country}'


def compare_accounts(accountA, accountB, user_choice):
    global PLAYER_SCORE
    if user_choice == 'A' and accountA['follower_count'] > accountB['follower_count']:
        PLAYER_SCORE += 1
    elif user_choice == 'B' and accountA['follower_count'] < accountB['follower_count']:
        PLAYER_SCORE += 1
    else:
        return 0


def game():
    global IS_GAME_FINISHED
    first_account = get_account()
    second_account = get_account()
    while not IS_GAME_FINISHED:
        first_account = second_account
        second_account = get_account()
        while first_account == second_account:
            second_account = get_account()

        print(f'Compare A: {format_data(first_account)}')
        print(art.vs)
        print(f'Compare B: {format_data(second_account)}')
        choice = input("Who has more followers? Type 'A' or 'B' ").upper()

        check_account = compare_accounts(first_account, second_account, choice)
        if check_account == 0:
            IS_GAME_FINISHED = True
            print(f"Sorry, that's wrong. Final score: {PLAYER_SCORE}")


if __name__ == '__main__':
    print(art.logo)
    game()
