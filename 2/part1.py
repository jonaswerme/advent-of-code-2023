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


def extract_stats(picked: str) -> dict:
    """Extract numbers from a string and return a list of numbers."""
    colors = ["red", "green", "blue"]
    result = {}
    for color in colors:
        if color not in picked:
            continue

        r_color = re.compile(r"(\d+) " + color)
        matches = r_color.findall(picked)
        if matches:
            result[color] = int(matches[0])

    return result


def main():
    """Main function."""

    games = {}
    for line in read_input("input"):
        # Extract the game metadata and data
        game_id = int(line.split(":")[0].strip().replace("Game ", ""))
        game_data = line.split(":")[1].strip()

        games[game_id] = {"red": 0, "green": 0, "blue": 0}

        # Split the game data on ;
        picks = game_data.split(";")
        for pick in picks:
            # Extract the stats from the pick
            pick_stats = extract_stats(pick)
            for color, stat in pick_stats.items():
                if games[game_id][color] < stat:
                    games[game_id][color] = stat

    # Game validation metadata
    validator = {"red": 12, "green": 13, "blue": 14}

    # Produce result
    game_id_sum = 0
    for game, data in games.items():
        valid = True
        for color, amount in validator.items():
            if amount < data[color]:
                print(f"Game {game} is invalid")
                valid = False
                break

        if valid:
            print(f"Game {game} is valid")
            game_id_sum += game

    print(f"Game id sum: {game_id_sum}")


if __name__ == "__main__":
    sys.exit(main())
