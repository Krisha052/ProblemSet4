
import emoji

def main():
    phrase = input("Input: ")
    print(emoji.emojize(f"Output: {phrase}", language="alias"))

if __name__ == "__main__":
    main()
