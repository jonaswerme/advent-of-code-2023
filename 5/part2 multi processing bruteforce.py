#!/bin/python3
"""
Advent of Code 2023
"""

import gc
import os
import sys
from multiprocessing import Pool


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


def generate_plants(seeds, data):
    """Generate a plant map"""
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

    return plants


def compute_lowest_location(plants):
    """Extract locations from plants and return the lowest location id"""
    lowest = 0
    for _, metadata in plants.items():
        lowest = (
            metadata["location"]["id"]
            if metadata["location"]["id"] < lowest or lowest == 0
            else lowest
        )

    return lowest


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
            seeds1 = [int(i) for i in line.split(":")[1].split(" ") if i]
            seeds2 = []
            it = iter(seeds1)
            for x in it:
                stop = x + int(next(it))
                print(x, stop)
                seeds2.append((x, stop))

            continue
        if ":" in line:
            data_set = line.split(" ")[0]
            continue

        map_name = data_set.split("-")[2].strip()
        if map_name not in data:
            data[map_name] = []

        data[map_name].append(parse_data(line))

    # Structure data into plant map for printability and easier to understand
    plants1 = generate_plants(seeds1, data)
    params = []
    for start, end in seeds2:
        params.append({"start": start, "end": end, "data": data})

    with Pool(os.cpu_count()) as p:
        values = p.map(process, params)

    lowest = 99999999999999999
    for lowest_location in values:
        if lowest_location < lowest:
            lowest = lowest_location

    # plants2 = generate_plants(seeds2, data)

    print("Part1 - Lowest location: ", compute_lowest_location(plants1))
    print("Part2 - Lowest location: ", lowest)


def process(params):
    """Process a given batch and return the lowest location id found"""
    lowest = 99999999999999
    start = params["start"]
    end = params["end"]
    data = params["data"]

    tmp_list = list(range(start, end))
    for i, batch in enumerate(chunk(tmp_list, 1000000)):
        print("Batch", i)
        tmp_plants = generate_plants(batch, data)
        tmp_lowest = compute_lowest_location(tmp_plants)
        if lowest > tmp_lowest:
            lowest = tmp_lowest
            print("New lowest", lowest)
        del tmp_plants
        del batch
        gc.collect()

    del tmp_list
    gc.collect()

    print("Local lowest", lowest)

    return lowest


def chunk(seq, size):
    """Chunk a list into smaller lists of given size"""

    for pos in range(0, len(seq), size):
        yield seq[pos : pos + size]

    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


if __name__ == "__main__":
    sys.exit(main())
