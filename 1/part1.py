#!/bin/python3
"""
Advent of Code 2023
"""
import os
import sys


def read_input(filename):
    """Read a file and return a generator of lines."""
    with open(f"{os.path.dirname(__file__)}/{filename}", "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def extract_numbers(line):
    """Extract numbers from a string and return a list of numbers."""
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append(int(char))
    return numbers


def main():
    """Main function."""

    sum_total = 0
    for line in read_input("input"):
        numbers = extract_numbers(line)

        calibration_value = f"{numbers[0]}{numbers[-1]}"

        sum_total += int(calibration_value)

    print(f"Sum total: {sum_total}")


if __name__ == "__main__":
    sys.exit(main())
