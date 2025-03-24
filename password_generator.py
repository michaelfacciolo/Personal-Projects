import random
import string

def generate_password(length, chars):
    """Generate a random password of given length using provided characters."""
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print('Welcome to the Password Generator!')

    chars = string.ascii_letters + string.digits + "!@£$%^&*().,?"

    while True:
        try:
            number = int(input('Amount of passwords to generate: '))
            length = int(input('Input your password length: '))
            if number <= 0 or length <= 0:
                print("Please enter positive integers for both values.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    print('\nHere are your passwords:')
    for _ in range(number):
        print(generate_password(length, chars))

if __name__ == "__main__":
    main()
