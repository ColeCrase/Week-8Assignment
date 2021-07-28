"""
Program: Project1
Author: Cole Crase
This program is to allow the user to input a number and then returns an estimate
of its square root.
"""

import math
tolerance = 0.000001
def newton(x):
    """Returns the square root of x"""
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
        return estimate
def main():
    """Allows the user to obtain square roots."""
    while True:
        x = input("Enter a positive number or press enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        print("The estimate of the square root of ", x, "is ",
               round(newton(x),2))
main()
