"""
Practice: Quadratic Formula Program

This program calculates the roots of a quadratic equation
using the general (quadratic) formula.

Author: Lalo Tellez
"""

from math import sqrt

print(f'{"=" * 20} General Formula {"=" * 20}\n')

condition = False

while not condition:

    a = float(input("A: "))

    if a != 0:
        condition = True

        b = float(input("B: "))
        c = float(input("C: "))

        # Calculate the discriminant
        discriminant = (b ** 2) - (4 * a * c)

        if discriminant < 0:
            print("\nThe equation has no real solutions.\n")
        else:
            square_root = sqrt(discriminant)

            x1 = (-b + square_root) / (2 * a)
            x2 = (-b - square_root) / (2 * a)

            print(f'\nX1 = {x1:.2f}')
            print(f'X2 = {x2:.2f}\n')
    else:
        print('A must not be 0. Try again.\n')

print(f'{"=" * 50}')
