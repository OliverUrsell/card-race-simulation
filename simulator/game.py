from typing import Dict, Optional

from simulator.card import Suit
from simulator.constants import k_extra_cards, k_length_of_line
from simulator.game_state import GameState


class Game:

    @staticmethod
    def play_game(
            verbosity: int,
            length_of_line: int = k_length_of_line,
            extra_cards: Optional[Dict[Suit, int]] = k_extra_cards
    ) -> Suit:
        """
        Plays a game of card race and returns the suit that won the game
        :param length_of_line: The length of the line of cards to use in the game
        :param extra_cards: How many cards of different suits to add / remove from the deck
        :param verbosity: the amount of information to print to the console:
        Verbosity -1: print nothing
        Verbosity 0: print the game winner
        Verbosity 1: Also print each card that is drawn
        Verbosity 2: Also print all game states
        :return: The card suit that won the game
        :raises: IndexError if the deck ran out of cards
        """

        try:
            for card, state in GameState(length_of_line=length_of_line, extra_cards=extra_cards):
                print("Drew card: " + str(card)) if verbosity >= 1 else 1 + 1
                print(str(state)) if verbosity >= 2 else 1 + 1
                print() if verbosity >= 1 else 1 + 1
        except IndexError:
            # The deck ran out of cards
            print("Nobody won, the deck ran out of cards!") if verbosity >= 0 else 1 + 1
            print("\n" + str(state)) if verbosity >= 2 else 1 + 1
            raise

        print(card.suit.to_full_name().capitalize() + "s won the game!") if verbosity >= 0 else 1 + 1
        print("\n" + str(state)) if verbosity >= 2 else 1 + 1

        return card.suit


if __name__ == '__main__':
    print("This file should not be run as main, run single_game.py or multiple_games.py instead")
