import random

def flip():
    match input("(H)eads, (T)ails, or (Q)uit: ").upper():
        case "Q":
            return False
        case "H":
            if random.randint(0, 1) == 0:
                print("Correct, it was heads!")
            else:
                print("Incorrect, it was tails.")
            return True
        case "T":
            if random.randint(0, 1) == 0:
                print("Correct, it was tails!")
            else:
                print("Incorrect, it was heads.")
            return True


def main():
    while True:
        if not flip():
            break
        print()

if __name__ == "__main__":
    main()
