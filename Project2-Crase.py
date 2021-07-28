"""
Program: Project2
Author: Cole Crase
This program is modify from project 1 that uses a recursive function.
As well as using the estimate of the square roote as a second argument.
"""

import math
tolerance = 0.000001
def newton(x, estimate):
    """Returns the square root of x"""
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            return estimate
        else:
            return newton(x,estimate)
def main():
    """Allows the user to obtain square roots."""
    while True:
        x = input("Enter a positive number or press enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        estimate = 1.0
        print("The estimate of the square root of ", x, "is ",
               round(newton(x, estimate)))
main()
