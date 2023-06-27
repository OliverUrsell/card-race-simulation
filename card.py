from enum import Enum


class Suit(Enum):
    HEART = 1
    DIAMOND = 2
    SPADE = 3
    CLUB = 4

    def __str__(self):
        if self == Suit.HEART:
            return "H"
        elif self == Suit.DIAMOND:
            return "D"
        elif self == Suit.SPADE:
            return "S"
        elif self == Suit.CLUB:
            return "C"
        else:
            raise ValueError("Suit cannot be represented as a string")


class Card:
    def __init__(self, value: int, suit: Suit):
        assert value < 14, "Can't create a card with value > 13"
        assert value > 0, "Can't create a card with value < 1"

        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        return str(self.value) + str(self.suit)
