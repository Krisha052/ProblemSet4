""" 
Program planning:
- Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and n, inclusive, using the random module.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    - If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    - If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    - If the guess is the same as that integer, the program should output Just right! and exit.
"""
import random

def main():
    level = get_positive_int("Level: ")
    number = random.randint(1, level)

    while True:
        guess = get_positive_int("Guess: ")
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass

if __name__ == "__main__":
    main()

