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

    def to_full_name(self):
        if self == Suit.HEART:
            return "Heart"
        elif self == Suit.DIAMOND:
            return "Diamond"
        elif self == Suit.SPADE:
            return "Spade"
        elif self == Suit.CLUB:
            return "Club"
        else:
            raise ValueError("Suit cannot be represented as a string")


class Card:
    def __init__(self, value: int, suit: Suit):
        assert value < 14, "Can't create a card with value > 13"
        assert value > 0, "Can't create a card with value < 1"

        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self) -> str:
        value_string: str = str(self.value)
        if value_string == "11":
            value_string = "J"
        elif value_string == "12":
            value_string = "Q"
        elif value_string == "13":
            value_string = "K"
        elif value_string == "1":
            value_string = "A"

        return value_string + str(self.suit)

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit
