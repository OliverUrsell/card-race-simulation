from typing import Dict, List

from simulator.card import Suit, Card
from simulator.constants import k_length_of_line
from simulator.deck import Deck


class GameState:
    _ace_positions: Dict[Suit, int]
    _side_cards: List[Card]
    _side_cards_revealed: int  # The number of side cards that have been overturned
    _deck: Deck
    _length_of_line: int

    def __init__(self, length_of_line=k_length_of_line):
        """Provide a constructor to override constants for testing"""
        self._length_of_line = length_of_line

    def __iter__(self):
        """Initialise the starting game state"""

        # Create an in-order deck
        self._deck = Deck()
        # Shuffle it
        self._deck.shuffle()

        # TODO: add extra cards through some configuration

        # Remove the aces from the deck
        for suit in Suit:
            self._deck.remove_card(Card(1, suit))

        # Initialise ace positions
        self._ace_positions = dict()
        for suit in Suit:
            self._ace_positions[suit] = 0

        # Draw cards for the side
        self._side_cards = []
        for _ in range(self._length_of_line):
            self._side_cards.append(self._deck.take_top())
        self._side_cards_revealed = 0

        return self

    def _done(self) -> bool:
        """Returns if the game is finished"""
        for suit in Suit:
            if self._ace_positions[suit] > self._length_of_line:
                return True
        return False

    def __next__(self):
        """Each time the iterator next is called, draw a card and update the game accordingly"""

        if self._done():
            # The game has finished so stop iterating
            raise StopIteration

        # Draw a card from the top of the deck
        card = self._deck.take_top()
        self._ace_positions[card.suit] += 1

        # Check to see whether all aces are now past a non-revealed side card
        all_past = True
        for suit in Suit:
            if self._ace_positions[suit] < self._side_cards_revealed + 2:
                all_past = False
                break

        if all_past:
            # Get the side card suit, lower the ace position of that suit by one
            revealed_suit = self._side_cards[self._side_cards_revealed].suit
            # self._ace_positions[revealed_suit] = max(0, self._ace_positions[revealed_suit] - 1)
            self._ace_positions[revealed_suit] -= 1
            self._side_cards_revealed += 1

        return card, self  # Return the new game state and the card drawn

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        out = ""
        for i in range(self._length_of_line + 1, -1, -1):
            # Go backwards from the length of the line to 0

            # Print the side cards
            if 0 < i < self._length_of_line + 1:
                # This is not the first or last line
                if i <= self._side_cards_revealed:
                    # This card is revealed
                    out += " " + str(self._side_cards[i-1]) + " "
                else:
                    out += " -- "
            else:
                out += "    "

            # Print the aces for this row
            for suit in Suit:
                if self._ace_positions[suit] == i:
                    out += " " + str(Card(1, suit)) + " "
                else:
                    out += " -- "

            # Remove extra whitespace
            out = out[:-1]

            out += "\n"
        return out
