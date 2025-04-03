import random

target = random.randint(1, 101)
remainingGuesses = 7

def start():
    max = int(input("\033[1;34mEnter the upper bound: \033[0m"))
    global target, remainingGuesses
    target = random.randint(1, max + 1)
    remainingGuesses = 0
    while (max > 1):
        max = max // 2 if max % 2 == 0 else (max + 1) // 2
        remainingGuesses += 1


def play():
    global remainingGuesses
    while remainingGuesses > 0:
        guess = int(input("\033[1;36mEnter a number: \033[0m"))
        if guess == target:
            print("\033[0;32mYou won! The number was\033[0m", target)
            break
        elif guess < target:
            print("\033[1;31mThe number is greater than\033[0m", guess)
        elif guess > target:
            print("\033[0;31mThe number is less than\033[0m", guess)
        remainingGuesses -= 1

    if remainingGuesses == 0:
        print("The number was", target)


def main():
    start()
    while True:
        play()
        match input("\033[1;34mDo you want to play again (y/n)? \033[0m").lower():
            case "y":
                continue
            case default:
                print("Goodbye!")
                break


if __name__ == "__main__":
    main()