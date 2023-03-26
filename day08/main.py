import string
import art


def caesar(message, shift_amount, choice):
    alphabet = string.ascii_lowercase
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    final_message = ''
    for char in message:
        if char in alphabet:
            idx = alphabet.index(char)
            if choice == 'encode':
                new_position = (idx + shift_amount) % 26
                char = alphabet[new_position]
            elif choice == 'decode':
                new_position = (idx - shift_amount) % 26
                char = alphabet[new_position]
            final_message += char
        else:
            final_message += char
    print(f'The {choice}d text is {final_message}')


def main():
    want_end = False
    while not want_end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(message=text, shift_amount=shift, choice=direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
        if restart == 'no':
            want_end = True


if __name__ == '__main__':
    print(art.logo)
    main()
