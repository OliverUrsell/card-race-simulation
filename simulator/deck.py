from random import shuffle
from typing import List

from simulator.card import Card, Suit


class Deck:

    _cards: List[Card]

    def __init__(self, start_full: bool = True):
        """
        :param start_full: Whether to start with an ordered deck (True), or an empty deck (False)
        """
        self._cards = []
        if start_full:
            for suit in Suit:
                for value in range(1, 14):
                    self.add_card(Card(value, suit))

    def add_card(self, card: Card):
        """
        Add the given card to the end of the deck
        :param card: The card to add to the end of the deck
        """
        self._cards += [card]

    def remove_card(self, card: Card):
        """
        Remove the first instance of the given card from the deck
        :param card: The card to remove
        :raises: ValueError if the card is not present
        """
        self._cards.remove(card)

    def __str__(self):
        """Provides a string representation for the deck"""
        return str(self._cards)

    def shuffle(self):
        """Shuffles the cards in the deck into a random order"""
        shuffle(self._cards)

    def __contains__(self, item: Card):
        """Allows checking if a card is in the deck using the 'in' operator"""
        return item in self._cards

    def copy(self):
        """
        Creates a copy of the deck containing the same cards in the same order but at a different reference location
        """
        new_deck = Deck(start_full=False)
        new_deck._cards = self._cards.copy()
        return new_deck

    def __getitem__(self, item: int):
        """Allows getting a card at a specific position in the deck using the square bracket operator"""
        return self._cards[item]

    def __len__(self):
        """Allows getting the number of cards in the deck using the standard 'len' function"""
        return len(self._cards)

    def take_top(self) -> Card:
        """Take the top card from the deck"""
        return self._cards.pop(0)
