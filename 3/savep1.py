#!/bin/python3

import sys
import os
import re

def read_input(filename):
    """Read a file and return a generator of lines."""
    with open(f"{os.path.dirname(__file__)}/{filename}", "r") as f:
        for line in f:
            yield line.strip()


def main():
    """Main function."""
    data = []

    numbers = []
    symbols = []
    
    for i, line in enumerate(read_input("input")):
        row = []
        for j, char in enumerate(line):
            if char.isdigit() or char == ".":
                row.append(char)
            else:
                row.append("x")
                symbols.append({
                    "row": i,
                    "column": j
                })

        data.append(row)

        
        line_numbers = re.findall(r"\d+", line)

        for number in line_numbers:
            numbers.append({
                "row": i,
                "start": line.find(number),
                "end": line.find(number) + len(number) - 1,
                "value": int(number)
            })

    legit_values = []

    for number in numbers:
        adjacent_symbol = False

        # Apparently we should not be counting douplicates(?)
        if number["value"] in legit_values:
            continue

        for symbol in symbols:
            prev_row = number["row"] - 1
            current_row = number["row"]
            next_row = number["row"] + 1

            if not symbol["row"] in [prev_row, current_row, next_row]:
                continue

            if symbol["column"] >= number["start"] - 1 and symbol["column"] <= number["end"] + 1:
                adjacent_symbol = True
                break

        if adjacent_symbol:
            legit_values.append(number["value"])

    # seen = set()
    # dupes = [x for x in legit_values if x in seen or seen.add(x)]
    # print(dupes)
    print(data)
    print("Sum of numbers: ", sum(legit_values))
        
            
        


if __name__ == "__main__":
    sys.exit(main())
