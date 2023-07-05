from random import shuffle
from typing import List

from simulator.card import Card, Suit


class Deck:

    _cards: List[Card]

    def __init__(self, start_full:bool = True):
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

    def remove_card(self, card:Card):
        """
        Remove the first instance of the given card from the deck
        :param card: The card to remove
        :raises: ValueError if the card is not present
        """
        self._cards.remove(card)

    def __str__(self):
        return str(self._cards)

    def shuffle(self):
        shuffle(self._cards)

    def __contains__(self, item):
        return item in self._cards

    def copy(self):
        new_deck = Deck(start_full=False)
        new_deck._cards = self._cards.copy()
        return new_deck

    def __getitem__(self, item):
        return self._cards[item]

    def __len__(self):
        return len(self._cards)

    def take_top(self) -> Card:
        """Take the top card from the deck"""
        return self._cards.pop(0)
