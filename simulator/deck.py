import random
from random import shuffle
from typing import List, Dict, Optional

from simulator.card import Card, Suit


class Deck:

    _cards: List[Card]

    def __init__(self, start_full: bool = True,
                 extra_cards: Optional[Dict[Suit, int]] = None,
                 remove_cards: Optional[List[Card]] = None):
        """
        :param start_full: Whether to start with an ordered deck (True), or an empty deck (False)
        :param extra_cards: Adds and removes cards of certain suits as described in the dictionary
        :param remove_cards: A list of cards to remove on initialisation, these cards are removed before extra_cards is
         applied
        """
        self._cards = []
        if start_full:
            for suit in Suit:
                for value in range(1, 14):
                    self.add_card(Card(value, suit))

            # Remove the cards in remove_cards
            if remove_cards is not None:
                for card in remove_cards:
                    self.remove_card(card)

            for suit in Suit:
                # Add or remove extra cards for each suit according to the extra_cards dictionary
                if extra_cards is not None and suit in extra_cards:
                    extras = extra_cards[suit]
                    if extras > 0:
                        # Add cards with random values of the given suit
                        for i in range(extras):
                            self.add_card(Card(random.randint(1, 13), suit))
                    elif extras < 0:
                        # Remove cards of the given suit
                        for i in range(-extras):
                            found = False
                            # TODO: this can be made more efficient by only going through the list once,
                            #  instead of starting again each time a card of the right suit is found
                            for card in self:
                                if card.suit == suit:
                                    self.remove_card(card)
                                    found = True
                                    break
                            assert found, f"Could not find enough {suit.to_full_name()}s in the deck to remove"

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


if __name__ == '__main__':
    print("This file should not be run as main, run single_game.py instead")
