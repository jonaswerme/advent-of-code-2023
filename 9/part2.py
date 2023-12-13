#!/bin/python3
"""
Advent of Code 2023
"""

import os
import sys

from numpy import diff


def read_input(filename):
    """Read a file and return a generator of lines."""
    with open(f"{os.path.dirname(__file__)}/{filename}", "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def main():
    """Main function."""

    p1_sum = 0
    p2_sum = 0
    for line in read_input("input"):
        differences = []
        data = [int(x) for x in line.split(" ")]

        last_value = data[-1]
        first_value = data[0]

        while [x for x in data if x != 0]:
            difference = diff(data).tolist()
            differences.append(difference)
            data = difference

        first_prediction = 0
        last_prediction = 0
        for data_set in differences[::-1]:
            last_prediction = data_set[-1] + last_prediction
            first_prediction = data_set[0] - first_prediction
        p1_sum += last_prediction + last_value
        p2_sum += first_value - first_prediction

    print("Part 1 - Total sum: ", p1_sum)
    print("Part 2 - Total sum: ", p2_sum)


if __name__ == "__main__":
    sys.exit(main())
