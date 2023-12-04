#!/bin/python3

import sys
import os
import re

def read_input(filename):
    """Read a file and return a generator of lines."""
    with open(f"{os.path.dirname(__file__)}/{filename}", "r") as f:
        for line in f:
            yield line.strip()


def generate_card(line):
    """Extract numbers from a string and return a list of numbers.
    
    Args:
        line: string to extract numbers from.
        
    Returns:
            A tuple of the card id and a dict representing the card.
    """
    winners = []
    numbers = []

    metadata = line.split(":")
    id = [ i for i in metadata[0].split(" ") if i][1]
    line = metadata[1]
    
    data = line.split("|")
    winners = [ i for i in data[0].split(" ") if i]
    numbers = [ i for i in data[1].split(" ") if i]

    return int(id), { "winners": winners, "numbers": numbers, "score": 0, "copies": [] }


def calculate_score(id, cards):
    """Recursively calculate the score of a card.
    
    Using the card id, we can find the cards copies and calculate the score recursively."""
    score = 1

    for cid in cards[id]["copies"]:
        if cid not in cards:
            continue
        
        score += calculate_score(cid, cards)

    return score


def main():
    """Main function."""
    cards = {}
  
    for line in read_input("input"):
        id, card = generate_card(line)

        for winner in card["winners"]:
            if winner in card["numbers"]:
                card["score"] += 1

        if card["score"] > 0:
            copy_start = id + 1
            
            for i in range(copy_start, copy_start + card["score"]):            
                card["copies"].append(i)

        cards[id] = card


    p1score = 0
    p2score = 0
    for card in cards:
        score = cards[card]["score"]
        p1score += score if score <= 1 else 2 ** (score-1)
        p2score += calculate_score(card, cards)

    print("Part1 - Total score: ", p1score)
    print("Part2 - Total score: ", p2score)

if __name__ == "__main__":
    sys.exit(main())
