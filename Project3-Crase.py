"""
Program: Project3
Author: Cole Crase
This program is modify from project 2 that uses keyword arguement with
appropriate default value.
"""

import math
tolerance = 0.000001
def newton(x, estimate):
    """Returns the square root of x"""
    while True:
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            return estimate
        else:
            return newton(x, (estimate + x / estimate) / 2)
def main():
    """To allow the user to obtain the square roots."""
    while True:
        x = input("Enter a number or press enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        estimate = 1.0
        print("The estimate of the square root of ", x, "is ",
               round(newton(x, estimate)))
main()
