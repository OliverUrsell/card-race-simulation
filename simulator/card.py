from enum import Enum


class Suit(Enum):
    HEART = 1
    DIAMOND = 2
    SPADE = 3
    CLUB = 4

    def __str__(self):
        """Provide a single character string representation of the suit"""
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
        """Returns the full name of the suit"""
        if self == Suit.HEART:
            return "heart"
        elif self == Suit.DIAMOND:
            return "diamond"
        elif self == Suit.SPADE:
            return "spade"
        elif self == Suit.CLUB:
            return "club"
        else:
            raise ValueError("Suit cannot be represented as a string")


class Card:
    def __init__(self, value: int, suit: Suit):
        """
        Construct a card with a value and suit
        The values 1, 11, 12 and 13 are interpreted as an ace, jack, queen or king respectively
        """
        assert value < 14, "Can't create a card with value > 13"
        assert value > 0, "Can't create a card with value < 1"

        self.suit = suit
        self.value = value

    def __repr__(self):
        """Ensures that cards are represented correctly when converting other objects, such as lists, to a string"""
        return self.__str__()

    def __str__(self) -> str:
        """Provides a string representation of the card"""
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
        """Allows checking to see if two cards are equal based on their suit and value"""
        return self.value == other.value and self.suit == other.suit
