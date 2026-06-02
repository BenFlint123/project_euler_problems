"""
This is solution to 'problem Zero' from project euler
Problem Zero asks the user to return the sum of all the odd numbers
from the first 695,000 square numbers

The problem provides that the first 5 square numbers are:
[1, 4, 9, 16, 25]
The sum of the odd entries are then:
1 + 9 + 25 = 35
so the solution to enter in this example would be: 35
"""
import numpy as np


def get_odd_squares(max_val: int):
    values = np.arange(1, max_val+1)
    odd_vals = values[0::2]
    odd_squares = odd_vals ** 2
    return odd_squares.sum()


def main():
    print(get_odd_squares(695000))

if __name__ == "__main__":
    main()
