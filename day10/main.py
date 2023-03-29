from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculation():
    print(logo)
    num1 = float(input('What is the first number? '))

    for operation in operations:
        print(operation)

    is_finished = False
    while not is_finished:
        choice = input('Pick an operation ')
        num2 = float(input('What is the next number? '))
        if choice not in operations:
            print("Invalid operation!")
            continue

        calculation_function = operations[choice]
        answer = calculation_function(num1, num2)

        print(f'{num1} {choice} {num2} = {answer}')

        end_question = input(f'Type "y" to continue calculating with {answer}, type "n" to start new calculation, '
                             f'or type "s" to stop ')

        while end_question.lower() not in ("y", "n", "s"):
            end_question = input('Invalid input! Please try again: ')

        if end_question.lower() == "n":
            calculation()
            break
        elif end_question.lower() == "y":
            num1 = answer
        elif end_question.lower() == "s":
            is_finished = True


if __name__ == "__main__":
    calculation()
