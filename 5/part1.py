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


def parse_data(data):
    """Parse the data and return a list of structured items."""
    data = data.split(" ")

    return {
        "next_start": int(data[0]),
        "start": int(data[1]),
        "end": int(data[1]) + int(data[2]),
        "length": int(data[2]),
    }


def find_map_match(data, position):
    """Find the instance that matches the next_id."""
    for item in data:
        if item["start"] <= position <= item["end"]:
            return item

    return {}


def main():
    """Main function."""

    # Handle input
    data_set = ""
    data = {}
    for i, line in enumerate(read_input("input")):
        if line in ["\n", "\r\n"] or not line:
            data_set = ""
            continue
        if line.startswith("seeds:"):
            seeds = [int(i) for i in line.split(":")[1].split(" ") if i]
            continue
        if ":" in line:
            data_set = line.split(" ")[0]
            continue

        map_name = data_set.split("-")[2].strip()
        if map_name not in data:
            data[map_name] = []

        data[map_name].append(parse_data(line))

    # Structure data into plant map for printability and easier to understand
    plants = {}
    for seed in seeds:
        plants[seed] = {}
        position = seed
        data_maps = [
            "seed",
            "soil",
            "fertilizer",
            "water",
            "light",
            "temperature",
            "humidity",
            "location",
        ]

        for i, data_map in enumerate(data_maps):
            next_map = data_maps[i + 1] if i + 1 < len(data_maps) else None

            previous_map = data_maps[i]
            previous_id = position

            match = find_map_match(data[next_map], position) if next_map else {}
            if match:
                position = position - match["start"] + match["next_start"]

            plants[seed][data_map] = match
            plants[seed][previous_map]["id"] = previous_id

    # Compute answer
    lowest = 999999999999
    for _, metadata in plants.items():
        lowest = (
            metadata["location"]["id"]
            if metadata["location"]["id"] < lowest
            else lowest
        )

    print("Part1 - Lowest location: ", lowest)

    # Uncomment to print the plant structure, plants are named after the seed they grew from
    # for plant, data in plants.items():
    #     print(f"Plant {plant}:")
    #     for key, value in data.items():
    #         print(f"\t{key}: {value}")


if __name__ == "__main__":
    sys.exit(main())
