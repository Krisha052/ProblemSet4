
""" 
Program Planning:
- Expects zero or two command-line arguments:
    - Zero if the user would like to output text in a random font.
    - Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.
"""


import sys
import pyfiglet
from pyfiglet import Figlet

def main():
    if len(sys.argv) == 1:
        # No font specified, use random
        f = Figlet()
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font_name = sys.argv[2]
        try:
            f = Figlet(font=font_name)
        except pyfiglet.FontNotFound:
            sys.exit("Invalid font name")
    else:
        sys.exit("Invalid usage")

    phrase = input("Input: ")
    print(f.renderText(phrase))

if __name__ == "__main__":
    main()

