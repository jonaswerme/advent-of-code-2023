#!/bin/python3
"""
Advent of Code 2023
"""

import os
import sys
from math import lcm


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

    # Find the goal nodes
    stats = {}
    for start, node in nodes.items():
        if not start.endswith("A"):
            continue

        print("Start node: ", start)

        hops = 0
        current_node = node
        while not current_node["position"].endswith("Z"):
            for direction in directions:
                current_node = nodes[current_node[direction]]
                hops += 1
            if current_node["position"].endswith("Z"):
                print("After", hops, "hops we found:", current_node)
                stats[start] = hops
                break

    total = lcm(*stats.values())

    print("Part2 - Total hops: ", total)


if __name__ == "__main__":
    sys.exit(main())
