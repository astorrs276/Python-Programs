# Recreation of Wordle in Python - Pydle
import random

target_word_set = set()
target_word_list = []
guess_set = set()
current_word = ""
guess_record = []


def parse_target_word_list(filename):
    global target_word_list
    with open(filename) as file:
        for line in file:
            target_word_set.add(line.strip().lower())
    target_word_list = list(target_word_set)


def parse_guess_list(filename):
    with open(filename) as file:
        for line in file:
            guess_set.add(line.strip().lower())


def new_current_word():
    global current_word
    current_word = target_word_list.pop(random.randint(0, len(target_word_list) - 1))


def print_letter(letter, color_index):
    end = "\033[0m"
    bold = "\033[1m"
    color_list = ["\033[0;32m", "\033[1;33m", "\033[1;30m"]  # [green, yellow, grey]
    print(bold, color_list[color_index], letter, " ", end, sep="", end="")


def print_all():
    for i in range(len(guess_record)):
        print("\033[1;36m", i + 1, ": \033[0m", end="", sep="")
        for command in guess_record[i]:
            print_letter(command[0], command[1])
        print()
    print()


def check_guess(guess):
    guess_commands = []
    if guess == current_word:
        for letter in guess:
            guess_commands.append((letter, 0))
        guess_record.append(guess_commands)
        return 0
    if len(guess) != 5 or guess not in guess_set:
        return -1

    current_word_listed = list(current_word)
    for i in range(len(guess)):
        if guess[i] == current_word[i]:
            guess_commands.append((guess[i], 0))
            current_word_listed.remove(guess[i])
        elif guess[i] in current_word_listed:
            guess_commands.append((guess[i], 1))
            current_word_listed.remove(guess[i])
        else:
            guess_commands.append((guess[i], 2))
    guess_record.append(guess_commands)
    return 1


def main():
    global guess_record
    parse_guess_list("Games/data/pydle_accepted_input.txt")
    parse_target_word_list("Games/data/pydle_possible_solutions.txt")
    new_current_word()
    while True:
        guesses = 0
        while guesses < 6:
            match check_guess(input("\033[1;34mGuess: \033[0m").lower().strip()):
                case -1:
                    print("\033[0;31mInvalid Guess\033[0m")
                    print_all()
                    continue
                case 0:
                    print_all()
                    print("\033[1;32mYou win!\033[0m")
                    guesses = 50
                case 1:
                    print_all()
                    guesses += 1
        if guesses == 6:
            print("You lost. The word was" + current_word)

        match input("Would you like to play again (y/n)? ").lower():
            case "y":
                guess_record = []
                guesses = 0
                new_current_word()
                print()
                continue
            case default:
                print("Goodbye")
                break


if __name__ == "__main__":
    main()
