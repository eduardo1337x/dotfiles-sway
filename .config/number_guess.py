import sys
from random import randint
from time import sleep
from os import name, system


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


clear()
print("Number Guess Game")
print()
print("[1] - Easy")
print("[2] - Intermediate")
print("[3] - Hard")
print()
difficulty = int(input("Select the difficulty: "))
if difficulty < 1 or difficulty > 3:
    print()
    print("Choose a valid option from the menu!")
    sleep(2)
    sys.exit()

number = randint(1, 30 * difficulty)
chances = 5

clear()
print("The secret number is between 1 and {}.".format(difficulty * 30))
print()
while chances > 0:
    guess = int(input("Guess: "))
    if guess > difficulty * 30 or guess < 1:
        print("The secret number is between 1 and {}.".format(difficulty * 30))
        continue
    elif guess == number:
        print("Correct!")
        chances = -1
    else:
        if guess > number:
            chances = chances - 1
            print("Too high ({} chances remaining).".format(chances))
        else:
            chances = chances - 1
            print("Too low ({} chances remaining).".format(chances))
    print()
    sleep(1)

if chances == 0:
    print("No chances remaining. Better luck next time!")
else:
    print("Congratulations! You guessed the secret number!")
print("The secret number was {}.".format(number))
sleep(2)
