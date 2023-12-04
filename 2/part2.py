#!/bin/python3

import sys
import os
import re

def read_input(filename):
    """Read a file and return a generator of lines."""
    with open(f"{os.path.dirname(__file__)}/{filename}", "r") as f:
        for line in f:
            yield line.strip()

def extract_stats(picked: str) -> dict:
    """Extract numbers from a string and return a list of numbers."""
    colors = ['red', 'green', 'blue']
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
        
        games[game_id] = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
        
        # Split the game data on ;
        picks = game_data.split(";")
        for pick in picks:
            # Extract the stats from the pick
            pick_stats = extract_stats(pick)
            for color in pick_stats:
                if games[game_id][color] < pick_stats[color]:
                    games[game_id][color] = pick_stats[color]
        
    # Produce result
    power_sum = 0
    for game in games:
        power = games[game]["red"] * games[game]["green"] * games[game]["blue"]
        print(f"Game {game} power: {power}")

        power_sum += power

    print(f"Power: {power_sum}")
        
       


if __name__ == "__main__":
    sys.exit(main())