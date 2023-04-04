MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_cash():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_transaction(total_money, drink_cost):
    global profit
    if total_money >= drink_cost:
        if total_money >= drink_cost:
            print('No change needed.')
        else:
            change = round(total_money - drink_cost)
            print(f'Here is ${change} dollars in change. ')
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(user_choice, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {user_choice}. Enjoy!')


def main_action():
    is_on = True
    while is_on:
        choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if choice in MENU:
            drink = MENU[choice]
            if check_resources(drink['ingredients']):
                if check_transaction(process_cash(), drink['cost']):
                    make_coffee(choice, drink['ingredients'])
        elif choice == 'report':
            water = resources['water']
            milk = resources['milk']
            coffee = resources['coffee']
            money = profit
            print(f'Water: {water} ml\nMilk: {milk} ml\nCoffee: {coffee}g\nMoney: ${money}')
        elif choice == 'off':
            is_on = False


if __name__ == '__main__':
    main_action()
