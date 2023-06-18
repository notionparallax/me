"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!

def validate_input(response):
    try:
        number = int(response)
        return number
    except ValueError:
        return None

def get_user_guess(low, high):
    while True:
        response = input("Enter your guess between {} and {}: ".format(low, high))
        number = validate_input(response)
        if number is not None:
            if low <= number <= high:
                return number
            else:
                print("Number out of bounds. Try again.")
        else:
            print("Invalid input. Please enter a number.")

def advancedGuessingGame():
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    target_number = random.randint(low, high)
    attempts = 0

    while True:
        guess = get_user_guess(low, high)
        attempts += 1

        if guess == target_number:
            return "You got it! It took you {} attempts.".format(attempts)
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")



if __name__ == "__main__":
    print(advancedGuessingGame())
