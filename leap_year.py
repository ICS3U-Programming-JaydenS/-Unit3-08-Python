#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 19, 2025
# This program tells you when a leap year is


def main():

    # Get the users year
    user_year_as_string = input("What year is it? :")

    # Checks if the user entered a number
    try:
        user_year_as_int = int(user_year_as_string)

        # Checks if the user's number is positive
        if user_year_as_int < 0:
            print("This program only works for positive numbers")

        # If it is positive it continues by dividing by 4 and checking if theres a remainder
        else:
            if user_year_as_int % 4 == 0:
                if user_year_as_int % 100 != 0:
                    print("Its a leap year!")

                # If there is then it checks for the other steps for the leap year
                else:
                    if user_year_as_int % 400 == 0:
                        print("It is a leap year!")

                    else:
                        print("It is not a leap year")

            # If it was not divisible by 4 this happens
            else:
                print("It is not a leap year!")
    except Exception:

        # If it  is not a integer this happens
        print((user_year_as_string), "is not a number")


if __name__ == "__main__":
    main()
