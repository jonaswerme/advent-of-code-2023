#!/bin/python3
"""
Advent of Code 2023
"""

import math
import os
import sys


def read_input(filename):
    """Read a file and return a generator of lines."""
    with open(f"{os.path.dirname(__file__)}/{filename}", "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def extract_numbers(line) -> list:
    """Extract numbers from a string and return a list of numbers.

    Args:
        line: string to extract numbers from.

    Returns:
            A list of our numbers.
    """
    # Remove metadata and keep numbers
    line = line.split(":")[1].strip()

    return [int(x) for x in line.split(" ") if x]


def calculate_wins(time, distance) -> int:
    """Calculate possible wins for the race

    Args:
        time: total time in ms
        distance: total distance in mm

    Returns:
        Number of wins
    """
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

    # Handle input
    for line in read_input("input"):
        if line.startswith("Time"):
            times = extract_numbers(line)
        elif line.startswith("Distance"):
            distances = extract_numbers(line)

    # Part 1
    wins = []
    for time, distance in zip(times, distances):
        wins.append(calculate_wins(time, distance))

    print("Part1 - Total score: ", math.prod(wins))

    # Part 2
    time = int("".join(str(i) for i in times))
    distance = int("".join(str(i) for i in distances))

    print("Part2 - Total score:", calculate_wins(time, distance))


if __name__ == "__main__":
    sys.exit(main())
