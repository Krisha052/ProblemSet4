"""
Program planning:
- Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
- Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits. 
No need to support operations other than addition (+).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE 
and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after 
three tries, the program should output the correct answer.
- The program should ultimately output the user’s score: the number of correct answers out of 10.
"""

import random


def main():
    level = get_level()
    while True:
        x, y = generate_integer(level)
        answer = int(input(f"{x} + {y} = "))
        tries = 0
        score = 0
        if tries < 3:
            if answer == x+y:
                score += 1
                break
            else:
                print("EEE")
                tries += 1
        else:
            print(f"{x} + {y} = {x+y}")
            tries = 0
        break
    print(f"Score: {score}")



def get_level():
    while True:
        level = input("Level: ")
        if level in [1,2,3]:
            break
        else:
            continue
    return level


def generate_integer(level):
    try:
        for x, y in range(1, 10):
            x = random.randint(1, level*10)
            y = random.randint(1, level*10)
    except ValueError:
        raise ValueError
    return x, y


if __name__ == "__main__":
    main()