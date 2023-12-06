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
        # Assignment is not covering concatenation of number texts where two numbers share a letter.
        # Apparently this should be treated individually so we keep first and last letters and
        # inject the number into the text instead of replacing the whole text.
        number_map = {
            "zero": "z0ro",
            "one": "o1ne",
            "two": "t2o",
            "three": "thr3e",
            "four": "fo4r",
            "five": "fi5e",
            "six": "s6x",
            "seven": "se7ven",
            "eight": "ei8gt",
            "nine": "ni9e",
        }

        # Find inxexes of numbers represented by text and sort them in order of occurance
        occurances = {}
        for number in number_map:
            if number in line:
                occurances[number] = line.index(number)
        replacements = dict(sorted(occurances.items(), key=lambda x: x[1]))

        # Replace text with numbers
        for number in replacements:
            line = line.replace(number, number_map[number])

        numbers = extract_numbers(line)

        calibration_value = f"{numbers[0]}{numbers[-1]}"

        sum_total += int(calibration_value)

    print(f"Sum total: {sum_total}")


if __name__ == "__main__":
    sys.exit(main())
