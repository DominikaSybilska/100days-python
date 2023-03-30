import random
import os

clear = lambda: os.system('cls')
CARD_VALUES = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(CARD_VALUES)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer has a blackjack, you lose"
    elif user_score == 0:
        return "You have a blackjack, you win!!"
    elif user_score > 21:
        return "You went over, you lose"
    elif computer_score > 21:
        return "Computer went over, you win!!"
    else:
        if user_score > computer_score:
            return "You win!"
        else:
            return "You lose"


def play_game():
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or user_score > 21 or computer_score == 0:
            is_game_over = True
        else:
            continue_play = False
            while not continue_play:
                next_card = input("Do you want another card? Type 'y' or 'n': ")
                if next_card == 'y':
                    user_cards.append(deal_card())
                    continue_play = True
                elif next_card == 'n':
                    continue_play = True
                    is_game_over = True
                else:
                    print("Invalid input. Please type 'y' or 'n'.")
            while computer_score <= 17 and not is_game_over:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            print(compare_scores(user_score, computer_score))
            again_question = input("Do you want to play again? Type 'y' or 'n': ")
            if again_question == 'y':
                play_game()
                clear()
            elif again_question == 'n':
                return
            else:
                print("Invalid input. Please type 'y' or 'n'.")


if __name__ == '__main__':
    start_question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_question == 'y':
        play_game()
