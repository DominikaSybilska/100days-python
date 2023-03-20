import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if choice >= 3 or choice < 0:
    print('You typed an invalid number, you lose!')
else:
    what_you_can_choose = [rock, paper, scissors]

    print(what_you_can_choose[choice])

    computer_choice = random.randint(0, 2)
    computer_choice_img = what_you_can_choose[computer_choice]
    print(f'Computer chose:\n {computer_choice_img}')

    if computer_choice == 0 and choice == 1:
        print('You win')
    elif computer_choice == 1 and choice == 2:
        print('You win')
    elif computer_choice == 2 and choice == 1:
        print('You lose')
    elif computer_choice == 1 and choice == 0:
        print('You lose')
    elif computer_choice == 0 and choice == 2:
        print('You lose')
    elif computer_choice == 2 and choice == 0:
        print('You win')
    elif computer_choice == choice:
        print("It's draw")
    else:
        print('Not defined')
