"""
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5,
6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import numpy as np

def main():
    vals = np.arange(1, 1000)
    masked_vals = vals[(vals % 3 == 0) | (vals % 5 == 0)]
    print(masked_vals.sum())

if __name__ == "__main__":
    main()
