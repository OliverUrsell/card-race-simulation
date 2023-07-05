from simulator.card import Suit
from simulator.game_state import GameState


class Game:

    @staticmethod
    def play_game(verbosity: int) -> Suit:
        """
        Plays a game of card race and returns the suit that won the game
        :param verbosity: the amount of information to print to the console:
        Verbosity -1: print nothing
        Verbosity 0: print the game winner
        Verbosity 1: Also print each card that is drawn
        Verbosity 2: Also print all game states
        :return: The card suit that won the game
        :raises: IndexError if the deck ran out of cards
        """
        try:
            for card, state in GameState():
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
    print("This file should not be run as main, run main.py instead")
