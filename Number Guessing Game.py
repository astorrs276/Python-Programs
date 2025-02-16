import random

number = random.randint(1, 101)
remainingGuesses = 7

print(number)
while remainingGuesses > 0:
    remainingGuesses -= 1
    guess = int(input("Enter a number: "))
    if guess == number:
        print("You won! The number was", number)
        break
    elif guess < number:
        print("The number is greater than your guess of", guess)
    elif guess > number:
        print("The number is less than your guess of", guess)

if remainingGuesses == 0:
    print("The number was", number)