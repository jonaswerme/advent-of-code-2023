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


def extract_data(line) -> dict | str:
    """Extract data from a string.

    Args:
        line: string to extract data from.

    Returns:
            str, int: Data representing a ha
    """
    if "=" in line:
        data = line.split("=")
        position = data[0].strip()
        next_data = data[1].replace("(", "").replace(")", "").replace(" ", "")
        nexts = next_data.split(",")

        return {"position": position, "L": nexts[0], "R": nexts[1]}

    return line.strip()


def main():
    """Main function."""

    # Read input
    directions = ""
    nodes = {}

    # Handle input
    for line in read_input("input"):
        if not line or line in ["\n", "\r", "\r\n"]:
            continue

        data = extract_data(line)
        if isinstance(data, str):
            directions = data
            continue

        nodes[data["position"]] = data

    # Settings
    start = "AAA"
    goal = "ZZZ"

    # Find the goal node
    hops = 0
    current_node = nodes[start]
    while current_node["position"] != goal:
        for direction in directions:
            current_node = nodes[current_node[direction]]
            hops += 1

        if current_node["position"] == goal:
            print("Goal node: ", current_node)
            break

    print("Part1 - Total hops: ", hops)


if __name__ == "__main__":
    sys.exit(main())
