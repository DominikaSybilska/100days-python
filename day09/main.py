import os
import art

bids = {}
is_end = False

print(art.logo)
print('Welcome to the secret auction program')


def find_highest_bid(records):
    highest_bid = 0
    winner = ''
    for bidder in records:
        bid_amount = records[bidder]
        if bid_amount >= highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is: {winner} with a bid of {highest_bid}$')


while not is_end:
    name = input('What is your name? ')
    price = int(input('What is your bid? $'))
    bids[name] = price
    end_question = input('Are there any others bidders? Type yes or no ')
    if end_question == 'no':
        is_end = True
        find_highest_bid(bids)
    elif end_question == 'yes':
        os.system('cls')
        continue
    else:
        print('Invalid answer')
    print(bids)
