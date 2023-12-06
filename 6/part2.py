#!/bin/python3

import sys
import os
import re
import math

# Example data:
# Time:      7  15   30
# Distance:  9  40  200

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
            A list of our numbers.
    """
    numbers = []

    # Remove metadata and keep numbers
    line = line.split(":")[1].strip()

    return [int(x) for x in line.split(" ") if x]


def calculate_wins(time, distance):
    print("Distance to beat:", distance, "mm in", time, "ms")
    losses = 0
    races = 0

    for hold_time in range(0, time):
        acceleration_per_ms = 1
        races += 1
        speed = hold_time * acceleration_per_ms
        travel_time = time - hold_time
        
        if speed * travel_time <= distance:
            losses += 1
    
    return races - losses


def main():
    """Main function."""
    times = []
    distances = []
    total = 0
    
    # Handle input
    for i, line in enumerate(read_input("input")):
        if line.startswith("Time"):
            times = extract_numbers(line)
        elif line.startswith("Distance"):
            distances = extract_numbers(line)
    
    wins = []
    for time, distance in zip(times, distances):
        wins.append(calculate_wins(time, distance))

    # Calculate score
    print("Part1 - Total score: ", math.prod(wins))
    
    time = int(''.join(str(i) for i in times))
    distance = int(''.join(str(i) for i in distances))

    print("Part2 - Total score:", calculate_wins(time, distance))


if __name__ == "__main__":
    sys.exit(main())