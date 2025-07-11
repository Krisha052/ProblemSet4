def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            if len(names) == 1:
                print(f"Adieu, adieu, to {names[0]}")
            elif len(names) == 2:
                print(f"Adieu, adieu, to {names[0]} and {names[1]}")
            else:
                # All but the last two joined with commas
                print(f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}")
            break

if __name__ == "__main__":
    main()

