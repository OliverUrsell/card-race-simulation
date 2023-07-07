
from typing import Dict, Optional
from simulator.card import Suit

k_length_of_line = 3  # The length of the track the cards need to cover

# k_extra_cards modifies the deck of the game to include more or less of a given suit
# E.g: k_extra_cards: Dict[Suit, int] = {Suit.HEART: 2, Suit.DIAMOND: -1, Suit.SPADE: -2, Suit.CLUB: -10}
# Adds 2 hearts, removes a diamond, removes 2 spades and removes 10 clubs
k_extra_cards: Optional[Dict[Suit, int]] = {Suit.HEART: 0, Suit.DIAMOND: 0, Suit.SPADE: 0, Suit.CLUB: 0}

# ------- The constants below are for running multiple games to calculate the probability of the different suits winning

k_number_of_games = 100000  # The number of games to play to determine the probabilities


if __name__ == '__main__':
    print("This file should not be run as main, run single_game.py or multiple_games.py instead")
