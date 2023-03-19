print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_choice = input("You are on the crossroad. Where do you want to go? Left or right\n").lower()
if first_choice == 'left':
    second_choice = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait "
                          "for a boat. Type 'swim' to swim across.\n").lower()
    if second_choice.lower() == 'wait':
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors - red, yellow and "
                             "blue. Which colour do you choose?\n").lower()
        if third_choice == 'red':
            print("There is a room full of fire. You were burned by fire. Game Over")
        elif third_choice == 'blue':
            print("You have met the beast. You've been eaten. Game Over.")
        elif third_choice == 'yellow':
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game over")
