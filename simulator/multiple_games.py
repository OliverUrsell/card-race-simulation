from typing import Dict

from simulator.card import Suit
from simulator.constants import k_number_of_games
from simulator.game import Game
from tqdm import tqdm

if __name__ == '__main__':
    victories: Dict[Suit, int] = {suit: 0 for suit in Suit}
    deck_out_count: int = 0

    for i in tqdm(range(k_number_of_games),
                  desc="Playing games",
                  ascii=False, ncols=75):
        try:
            victories[Game().play_game(-1)] += 1
        except IndexError:
            # TODO: Make a custom error for the deck running out of cards
            # The deck ran out of cards
            deck_out_count += 1

    print("Complete.")

    for suit in Suit:
        probability = str(victories[suit]/k_number_of_games)
        print(f"{suit.to_full_name().capitalize()}s won {victories[suit]} games, win probability: {probability}")

    if deck_out_count > 0:
        probability = str(deck_out_count / k_number_of_games)
        print(f"The deck ran out of cards {deck_out_count} times, the probability of this happening is {probability}")
    else:
        print("The deck did not run out of cards for any games")
