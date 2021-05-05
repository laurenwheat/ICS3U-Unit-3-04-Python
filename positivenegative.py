#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program plays the number guessing game, but better


def main():
    # this function plays the number guessing game, but better

    guess = int(input("Enter a number: "))

    if guess < 0:
        print(guess)
        print("Is a negative number")
    elif guess > 0:
        print(guess)
        print("Is a positive number")
    elif guess == 0:
        print("0 is just 0")
    else:
        print("No idea!")


if __name__ == "__main__":
    main()
