#!/bin/python3
"""
Advent of Code 2023
"""

import os
import sys


class Node:  # pylint: disable=too-few-public-methods
    """Node class"""

    def __init__(self, position, left, right):
        """Initialize"""
        self.position = position
        self.left = left
        self.right = right

    def __str__(self):
        """Make a easy to read representation of the node
        Only prints the attributes that are have a set value
        Format:
            <attribute1>: <value1>, >

        Returns: str

        """
        representation = []
        for attribute, value in self.__dict__.items():
            if value is not None:
                representation.append(
                    f"{attribute.replace('_',' ').capitalize()}: {value}"
                )

        return ", ".join(representation)


def read_input(filename):
    """Read a file and return a generator of lines."""
    with open(f"{os.path.dirname(__file__)}/{filename}", "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def extract_data(line) -> Node | str:
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

        return Node(position, nexts[0], nexts[1])

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

        nodes[data.position] = data

    # Settings
    start = "AAA"
    goal = "ZZZ"

    # Find the goal node
    hops = 0
    current_node = nodes[start]
    while current_node.position != goal:
        for direction in directions:
            if direction == "L":
                current_node = nodes[current_node.left]
            elif direction == "R":
                current_node = nodes[current_node.right]
            hops += 1

            if current_node.position == goal:
                print("Goal node: ", current_node)
                break

    print("Part1 - Total hops: ", hops)


if __name__ == "__main__":
    sys.exit(main())
