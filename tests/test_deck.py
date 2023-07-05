import functools
import unittest

from simulator.card import Card, Suit
from simulator.deck import Deck


class TestDeck(unittest.TestCase):
    _expected_initial_deck: str = "[AH, 2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H, 10H, JH, QH, KH, AD, 2D, 3D, 4D, 5D, 6D, 7D, " \
                                  "8D, 9D, 10D, JD, QD, KD, AS, 2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S, 10S, JS, QS, KS, AC, " \
                                  "2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C, 10C, JC, QC, KC]"

    def test_string_conversion(self):
        """Test the conversion from a Deck class to a string"""
        deck = Deck(start_full=False)
        self.assertEqual("[]", str(deck))

        deck = Deck(start_full=True)
        self.assertEqual(self._expected_initial_deck, str(deck))

    def test_start_full_default(self):
        """Test that the deck starts full by default"""
        self.assertEqual(self._expected_initial_deck, str(Deck()))

    def test_add_card(self):
        """Test that adding cards to the deck works"""
        deck = Deck(start_full=False)
        self.assertEqual("[]", str(deck))

        deck.add_card(Card(1, Suit.DIAMOND))
        self.assertEqual("[AD]", str(deck))

    def test_remove_card(self):
        """Test that removing cards from the deck works"""
        deck = Deck(start_full=False)
        self.assertEqual("[]", str(deck))

        deck.add_card(Card(1, Suit.DIAMOND))
        self.assertEqual("[AD]", str(deck))

        deck.add_card(Card(3, Suit.HEART))
        self.assertEqual("[AD, 3H]", str(deck))

        deck.remove_card(Card(1, Suit.DIAMOND))
        self.assertEqual("[3H]", str(deck))

        self.assertRaises(ValueError, deck.remove_card, Card(1, Suit.DIAMOND))

    def test_shuffle_deck(self):
        """Test that shuffling the deck works"""
        deck = Deck()
        shuffled_deck = deck.copy()
        shuffled_deck.shuffle()

        # Check presence
        self.assertTrue(functools.reduce(lambda acc, curr: acc and (curr in shuffled_deck), deck), "The shuffled deck "
                                                                                                   "didn't contain all "
                                                                                                   "the same cards")

        # Check order has changed
        found = False
        for i, card in enumerate(deck):
            if card != shuffled_deck[i]:
                found = True
                break
        self.assertTrue(found, "The deck shuffle didn't change the order of the cards")

    def test_deck_contains(self):
        """Test checking if the deck contains a card"""
        deck = Deck(start_full=False)
        self.assertEqual("[]", str(deck))

        deck.add_card(Card(1, Suit.DIAMOND))
        self.assertEqual("[AD]", str(deck))

        self.assertTrue(Card(1, Suit.DIAMOND) in deck)

        self.assertFalse(Card(13, Suit.HEART) in deck)

    def test_deck_copy(self):
        """Test that copying the deck works"""
        deck = Deck()
        copied_deck = deck.copy()

        self.assertFalse(deck == copied_deck)

        # Check presence
        self.assertTrue(functools.reduce(lambda acc, curr: acc and (curr in copied_deck), deck), "The copied deck "
                                                                                                 "didn't contain all "
                                                                                                 "the same cards")

        # Check order hasn't changed
        found = False
        for i, card in enumerate(deck):
            if card != copied_deck[i]:
                found = True
                break
        self.assertFalse(found, "The copied deck had the wrong order")

    def test_take_first(self):
        """Test the function for taking the top card from the deck"""
        deck = Deck(start_full=False)
        self.assertEqual("[]", str(deck))

        deck.add_card(Card(1, Suit.DIAMOND))
        self.assertEqual("[AD]", str(deck))

        deck.add_card(Card(3, Suit.HEART))
        self.assertEqual("[AD, 3H]", str(deck))

        top = deck.take_top()
        self.assertEqual(Card(1, Suit.DIAMOND), top)
        self.assertEqual("[3H]", str(deck))

        deck.take_top()
        self.assertRaises(IndexError, deck.take_top)

    def test_len(self):
        """Tests that the len function correctly returns the number of cards in the deck"""
        deck = Deck(start_full=True)
        self.assertEqual(len(deck), 52)
        deck.take_top()
        self.assertEqual(len(deck), 51)
        deck.take_top()
        self.assertEqual(len(deck), 50)
        deck.take_top()
        deck.take_top()
        self.assertEqual(len(deck), 48)

        deck = Deck(start_full=False)
        self.assertEqual(len(deck), 0)


if __name__ == '__main__':
    unittest.main()
