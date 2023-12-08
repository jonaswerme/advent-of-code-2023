#!/bin/python3
"""
Advent of Code 2023
"""

import os
import sys
from typing import Tuple


def read_input(filename):
    """Read a file and return a generator of lines."""
    with open(f"{os.path.dirname(__file__)}/{filename}", "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def extract_data(line) -> Tuple[str, int]:
    """Extract hands and bids from a string.

    Args:
        line: string to extract numbers from.

    Returns:
            A tuple of two lists, first is are the winning numbers and second is our numbers.
    """
    data = line.split(" ")
    hand = data[0]
    bid = int(data[1])

    return hand, bid


class Card:
    """Card class"""

    # Note the position change of joker
    values = "J23456789TQKA"  # Order of value is important, index pos is used to compare cards

    def __init__(self, value):
        """Initialize"""
        if value not in Card.values:
            raise ValueError("Incorrect card value")

        self.value = value
        self.score = self.values.index(value)

    def __str__(self):
        """Return the value of the card."""
        return self.value

    def __lt__(self, comp):
        """Compare the score of two cards"""
        return self.score < comp.score

    def __gt__(self, comp):
        """Compare the score of two cards

        Not needed for the solution but nice to have."""
        return self.score > comp.score

    def __eq__(self, comp):
        """Compare the score of two cards

        Not needed for the solution but nice to have.
        """
        return self.score == comp.score


class Hand:
    """Hand class"""

    def __init__(self, cards, bid):
        """Initialize"""
        if len(cards) != 5:
            raise ValueError("Incorrect card count, must be 5 cards in a hand")

        self.bid = bid
        self.cards = [Card(c) for c in cards]
        self.card_values = [c.score for c in self.cards]
        self.power = self._get_power(cards)

    def __str__(self):
        """Return the value of the card.

        Not needed for the solution but nice to have."""
        return f"Cards: {[c.value for c in self.cards]} Power: {self.power} Bid: {self.bid}"

    def __lt__(self, comp):
        """Compare the power of two hands"""
        if self.power < comp.power:
            return True

        # Rules say we should compare card scores left to right if the score is the same
        if self.power == comp.power:
            for c1, c2 in zip(self.cards, comp.cards):
                if c1 < c2:
                    return True
                if c2 < c1:
                    break
        return False

    def __gt__(self, comp):
        """Compare the power of two hands"""
        if self.power > comp.power:
            return True

        # Rules say we should compare card scores left to right if the score is the same
        if self.power == comp.power:
            for c1, c2 in zip(self.cards, comp.power):
                if c1 > c2:
                    return True
                if c2 > c1:
                    break
        return False

    def __eq__(self, comp):
        """Compare the power of two hands"""
        if self.card_values == comp.card_values:
            return True
        return False

    def _get_power(self, cards: str):
        """Get the power of a hand.

        By calculating the count of each card value and sorting the result we can
        get a unique representation of a hands power.

        The sorted count maps to the point system in the rules.
        [5] = 5 of a kind
        [4, 1] = 4 of a kind
        [3, 2] = Full house
        [3, 1, 1] = 3 of a kind
        [2, 2, 1] = 2 pairs
        [2, 1, 1, 1] = 1 pair
        [1, 1, 1, 1, 1] = High card
        """
        unique_cards = set(cards)
        values = {}
        for card in unique_cards:
            values[card] = cards.count(card)

        # Handle jokers
        jokers = values.get("J", 0)
        if jokers:
            del values["J"]
        power = sorted(values.values(), reverse=True)

        # It is safe to only add jokers to highest power as we are limited to 5 cards
        # If we have a high card and a joker we will have a pair
        # If we have a pair and a joker we will have a full house
        # If we have a three of a kind and a joker we will have a four of a kind
        # If we have a four of a kind and a joker we will have a five of a kind
        # The joker will still be counted as lowest in the comparison (as rules define)

        if not power: # Corner case where we only have jokers
            power.append(jokers)  
        else:
            power[0] += jokers
        return power


def main():
    """Main function."""

    # Read input
    hands = []
    for line in read_input("input"):
        cards, bid = extract_data(line)

        hands.append(Hand(cards, bid))

    # Sort hands and let the classes compare functions do the work
    hands.sort()

    # Calculate winnings
    total = 0
    for i, hand in enumerate(hands):
        total += hand.bid * (i + 1)

    print("Part2 - Total score: ", total)


if __name__ == "__main__":
    sys.exit(main())
