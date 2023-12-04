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


def calculate_score(id, cards, oid):
    """Recursively calculate the score of a card.
    
    Using the card id, we can find the cards copies and calculate the score recursively."""
    score = 1

    for cid in cards[id]["copies"]:
        if cid not in cards:
            continue
        
        score += calculate_score(cid, cards, oid)

    return score


def main():
    """Main function."""
    cards = {}
    total = 0

    tally = {}
    
    for line in read_input("input"):
        id, card = generate_card(line)

        for winner in card["winners"]:
            if winner in card["numbers"]:
                card["score"] += 1

        if card["score"] == 0:
            cards[id] = card
            continue
        
        copy_start = id + 1

        for i in range(copy_start, copy_start + card["score"]):            
            card["copies"].append(i)

        cards[id] = card


    for card in cards:
        tally[card] = calculate_score(card, cards, card)
        total += tally[card]

    print("Part2 - Total score: ", total)

if __name__ == "__main__":
    sys.exit(main())
