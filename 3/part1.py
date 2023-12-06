#!/bin/python3
"""
Advent of Code 2023
"""

import os
import re
import sys


def read_input(filename):
    """Read a file and return a generator of lines."""
    with open(f"{os.path.dirname(__file__)}/{filename}", "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def main():
    """Main function."""
    numbers = []
    symbols = []

    for i, line in enumerate(read_input("input")):
        for j, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbols.append({"row": i, "column": j})

        line_numbers = re.finditer(r"\d+", line)

        for number in line_numbers:
            numbers.append(
                {
                    "row": i,
                    "start": number.start(),
                    "end": number.end() - 1,
                    "value": int(number.group()),
                }
            )

    legit_values = []

    for number in numbers:
        adjacent_symbol = False

        for symbol in symbols:
            prev_row = number["row"] - 1
            current_row = number["row"]
            next_row = number["row"] + 1

            if not symbol["row"] in [prev_row, current_row, next_row]:
                continue

            if (
                symbol["column"] >= number["start"] - 1
                and symbol["column"] <= number["end"] + 1
            ):
                adjacent_symbol = True
                break

        if adjacent_symbol:
            legit_values.append(number["value"])

    print("Part1 - Sum of numbers: ", sum(legit_values))


if __name__ == "__main__":
    sys.exit(main())
