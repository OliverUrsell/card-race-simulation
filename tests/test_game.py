import unittest.mock
import random
import io
from typing import Callable, Any

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
        self.assert_stdout(expected_value, lambda: Game().play_game(-1))

    def test_play_game_verbosity_0(self):
        """Test the output of a game with verbosity 0"""
        with open("expected_values/game/verbose_0_output.txt") as f:
            expected_value = f.read()

        random.seed(1234)
        self.assert_stdout(expected_value, lambda: Game().play_game(0))

    def test_play_game_verbosity_1(self):
        """Test the output of a game with verbosity 1"""
        with open("expected_values/game/verbose_1_output.txt") as f:
            expected_value = f.read()

        random.seed(1234)
        self.assert_stdout(expected_value, lambda: Game().play_game(1))

    def test_play_game_verbosity_2(self):
        """Test the output of a game with verbosity 2"""
        with open("expected_values/game/verbose_2_output.txt") as f:
            expected_value = f.read()

        random.seed(1234)
        self.assert_stdout(expected_value, lambda: Game().play_game(2))


if __name__ == '__main__':
    unittest.main()
