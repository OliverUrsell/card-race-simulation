
import unittest

from simulator.card import Card, Suit


class TestCard(unittest.TestCase):

    def test_string_conversion(self):
        """
        Test the conversion from a Card class to a string
        """
        self.assertEqual("3H", str(Card(3, Suit.HEART)))
        self.assertEqual("JD", str(Card(11, Suit.DIAMOND)))
        self.assertEqual("QS", str(Card(12, Suit.SPADE)))
        self.assertEqual("KC", str(Card(13, Suit.CLUB)))
        self.assertEqual("AS", str(Card(1, Suit.SPADE)))

    def test_invalid_card_values(self):
        """
        Tests that cards can't be created with a value of <1 or >13
        """
        self.assertRaises(AssertionError, Card, 0, Suit.DIAMOND)
        self.assertRaises(AssertionError, Card, 14, Suit.DIAMOND)

    def test_list_representation(self):
        """Tests that cards are represented properly when printing a list they are an element of"""
        cards = [Card(1, Suit.DIAMOND), Card(13, Suit.CLUB), Card(5, Suit.HEART)]
        self.assertEqual("[AD, KC, 5H]", str(cards))

    def test_equality(self):
        """
        Tests that two cards with the same suit and value are considered equal
        and tests that two cards without the same suit and/or value are not considered equal
        """
        self.assertEqual(Card(2, Suit.SPADE), Card(2, Suit.SPADE))
        self.assertNotEqual(Card(2, Suit.SPADE), Card(2, Suit.HEART))
        self.assertNotEqual(Card(2, Suit.SPADE), Card(13, Suit.SPADE))
        self.assertNotEqual(Card(2, Suit.SPADE), Card(13, Suit.HEART))

    def test_to_full_name(self):
        """Tests that suits are represented with the correct full name"""
        self.assertEqual("diamond", Suit.DIAMOND.to_full_name())
        self.assertEqual("heart", Suit.HEART.to_full_name())
        self.assertEqual("club", Suit.CLUB.to_full_name())
        self.assertEqual("spade", Suit.SPADE.to_full_name())


if __name__ == '__main__':
    unittest.main()
