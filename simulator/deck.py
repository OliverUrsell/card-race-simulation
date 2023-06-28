from random import shuffle
from typing import List

from simulator.card import Card, Suit


class Deck:

    _cards: List[Card]

    def __init__(self, start_full:bool = True):
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
        self._cards += card

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
