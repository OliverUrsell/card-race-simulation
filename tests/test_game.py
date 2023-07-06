import unittest.mock
import random
import io
from typing import Callable, Any

from simulator.card import Suit
from simulator.game import Game


class TestGame(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output: Any, func: Callable, mock_stdout: io.StringIO):
        """
        Assert an expected value for stdout (the content printed to the console)
        Usage:  self.assert_stdout(expected_value, func)
        Where expected_value is the string the function prints to the console and func is the function that calls print
        The mock_stdout parameter is provided by the decorator
        """
        func()
        self.assertEqual(expected_output, mock_stdout.getvalue())

    def test_play_game_verbosity_negative_1(self):
        """Test the output of a game with verbosity -1"""
        with open("expected_values/game/verbose_-1_output.txt") as f:
            expected_value = f.read()

        random.seed(1234)
        self.assert_stdout(expected_value, lambda: Game().play_game(-1, length_of_line=7, extra_cards=None))

    def test_play_game_verbosity_0(self):
        """Test the output of a game with verbosity 0"""
        with open("expected_values/game/verbose_0_output.txt") as f:
            expected_value = f.read()

        random.seed(1234)
        self.assert_stdout(expected_value, lambda: Game().play_game(0, length_of_line=7, extra_cards=None))

    def test_play_game_verbosity_1(self):
        """Test the output of a game with verbosity 1"""
        with open("expected_values/game/verbose_1_output.txt") as f:
            expected_value = f.read()

        random.seed(1234)
        self.assert_stdout(expected_value, lambda: Game().play_game(1, length_of_line=7, extra_cards=None))

    def test_play_game_verbosity_2(self):
        """Test the output of a game with verbosity 2"""
        with open("expected_values/game/verbose_2_output.txt") as f:
            expected_value = f.read()

        random.seed(1234)
        self.assert_stdout(expected_value, lambda: Game().play_game(2, length_of_line=7, extra_cards=None))

    def test_play_game_extra_cards(self):
        """Test the output of a game with verbosity 2 and extra cards specified"""
        with open("expected_values/game/verbose_2_extra_cards_output.txt") as f:
            expected_value = f.read()

        random.seed(1234)
        self.maxDiff = None
        self.assert_stdout(expected_value, lambda: Game().play_game(2, length_of_line=7, extra_cards={Suit.HEART: 2,
                                                                                                      Suit.DIAMOND: -1,
                                                                                                      Suit.SPADE: -2,
                                                                                                      Suit.CLUB: -10}))


if __name__ == '__main__':
    unittest.main()
