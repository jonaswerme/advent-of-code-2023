#!/bin/python3

import sys
import os
import re

def read_input(filename):
    """Read a file and return a generator of lines."""
    with open(f"{os.path.dirname(__file__)}/{filename}", "r") as f:
        for line in f:
            yield line.strip()

# Extract numbers from string as a list
def extract_numbers(line) -> (list,list):
    """Extract numbers from a string and return a list of numbers.
    
    Args:
        line: string to extract numbers from.
        
    Returns:
            A tuple of two lists, first is are the winning numbers and second is our numbers.
    """
    winners = []
    numbers = []

    # Remove metadata and keep numbers
    line = line.split(":")[1].strip()

    # Split numbers into two lists and remove empty strings
    data = line.split("|")
    winners = [ i for i in data[0].split(" ") if i]
    numbers = [ i for i in data[1].split(" ") if i]

    return winners, numbers
    

def main():
    """Main function."""
    winners = []
    total = 0
    
    for i, line in enumerate(read_input("input")):
        winners, numbers = extract_numbers(line)
        score = 0
        for winner in winners:
            if winner in numbers:
                numbers.remove(winner)
                score = 1 if score == 0 else score * 2

        print(f"Card {i + 1}: {score} losers: {numbers}")
        total += score

    print("Part1 - Total score: ", total)
        
            
if __name__ == "__main__":
    sys.exit(main())
