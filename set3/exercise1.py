# -*- coding: UTF-8 -*-
"""Set 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop, step=1):
    my_range = []
    for i in range(start, stop, step): 
        my_range.append(i)

    return my_range


def two_step_ranger(start, stop):
    two_step = []
    for i in range(start, stop, 2):
        two_step.append(i)

    return two_step



def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for a function called "input"
    """
    while True:
        try:
            number = int(input("Enter a number between {} and {}: " .format(low, high)))
            if low < number < high:
                return number
        except Exception:
            print("please try again")



def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        number = input(message)
        try:
            number = input(number)
            return number
        except Exception:
            print("That's not valid, please try again")



def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    """
    while True:
        try:
            number = int(input("Enter a number between {} and {}: " .format(low, high)))
            if low < number < high:
                return number
            else:
                print(
                    "That's not a number within the range, please try again"
                )
        except Exception:
            print("That's not valid, please try again")



if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
