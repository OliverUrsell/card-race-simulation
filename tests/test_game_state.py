import random
import unittest

from simulator.card import Suit, Card
from simulator.constants import k_length_of_line
from simulator.game_state import GameState


class TestGameState(unittest.TestCase):

    _expected_modified_suit_deck: str = "[7S, 5D, 4S, QH, 3H, 8D, 10S, 10H, 6S, 5H, KS, QC, 6H, 6D, 3S, 7D, JD, QD, " \
                                        "KH, 8S, 5S, 9S, KH, 8H, 2S, 8H, KC, 4H, 7H, 2H, 9H]"

    def test_iter(self):
        """Tests the initial setup of the game state iterator"""
        state = iter(GameState())

        # TODO: Test that the deck has been shuffled

        # Test that the number of side cards is correct
        self.assertEqual(k_length_of_line, len(state._side_cards))

        # Test the number of revealed side cards is correct
        self.assertEqual(0, state._side_cards_revealed)

        # Test that there are no aces in the deck
        for suit in Suit:
            self.assertTrue(Card(1, suit) not in state._deck)

        self.assertEqual(52 - 4 - k_length_of_line, len(state._deck))

        # Test the ace positions have been initialised correctly
        self.assertDictEqual({Suit.HEART: 0, Suit.DIAMOND: 0, Suit.SPADE: 0, Suit.CLUB: 0}, state._ace_positions)

    def test_next(self):
        """Test that the next function is incrementing the game state correctly"""
        state = iter(GameState(length_of_line=9))
        state._deck._cards = [Card(6, Suit.SPADE)]
        state._side_cards = [Card(9, Suit.SPADE), Card(12, Suit.HEART)]
        state._side_cards_revealed = 1
        state._ace_positions = {Suit.HEART: 4, Suit.DIAMOND: 5, Suit.SPADE: 2, Suit.CLUB: 5}

        # Increment the game state
        next(state)

        # Test that the ace position dictionary has been changed correctly
        self.assertDictEqual({Suit.HEART: 3, Suit.DIAMOND: 5, Suit.SPADE: 3, Suit.CLUB: 5}, state._ace_positions)

        # Test the number of side cards revealed is correct
        self.assertEqual(2, state._side_cards_revealed)

    def test_done(self):
        """Tests the _done function correctly checks if the game is finished or not"""
        state = iter(GameState(length_of_line=6))
        state._deck._cards = [Card(6, Suit.SPADE)]
        state._side_cards = [Card(9, Suit.CLUB), Card(12, Suit.HEART)]

        state._ace_positions = {Suit.HEART: 4, Suit.DIAMOND: 5, Suit.SPADE: 2, Suit.CLUB: 6}
        state._side_cards_revealed = 1
        self.assertFalse(state._done())

        state._ace_positions = {Suit.HEART: 4, Suit.DIAMOND: 5, Suit.SPADE: 2, Suit.CLUB: 7}
        self.assertTrue(state._done())

        # Test that stop iteration is raised after the game is finished
        self.assertRaises(StopIteration, state.__next__)

    def test_string(self):
        """Test the string representation of the game state"""

        state = iter(GameState(length_of_line=7, extra_cards=None))

        with open("expected_values/game_state/game_state_string_initial.txt") as f:
            expected_value = f.read()

        self.assertEqual(expected_value, str(state))

        state = iter(GameState(length_of_line=7, extra_cards=None))
        state._deck._cards = [Card(6, Suit.SPADE)]
        state._side_cards = [Card(9, Suit.SPADE), Card(12, Suit.HEART)]
        state._side_cards_revealed = 1
        state._ace_positions = {Suit.HEART: 4, Suit.DIAMOND: 5, Suit.SPADE: 2, Suit.CLUB: 5}

        with open("expected_values/game_state/game_state_string_before.txt") as f:
            expected_value = f.read()

        self.assertEqual(expected_value, str(state))

        next(state)

        with open("expected_values/game_state/game_state_string_after.txt") as f:
            expected_value = f.read()

        self.assertEqual(expected_value, str(state))

    def test_extra_cards(self):
        random.seed(1234)
        state = iter(GameState(length_of_line=7, extra_cards={Suit.HEART: 2, Suit.DIAMOND: -2, Suit.CLUB: -10}))
        self.assertEqual(self._expected_modified_suit_deck, str(state._deck._cards))


if __name__ == '__main__':
    unittest.main()
