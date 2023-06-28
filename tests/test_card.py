
import unittest

from simulator.card import Card, Suit


class TestCard(unittest.TestCase):

    def test_string_conversion(self):
        """
        Test the conversion from a Card class to a string
        """
        self.assertEqual(str(Card(3, Suit.HEART)), "3H")
        self.assertEqual(str(Card(11, Suit.DIAMOND)), "JD")
        self.assertEqual(str(Card(12, Suit.SPADE)), "QS")
        self.assertEqual(str(Card(13, Suit.CLUB)), "KC")
        self.assertEqual(str(Card(1, Suit.SPADE)), "AS")

    def test_invalid_card_values(self):
        """
        Tests that cards can't be created with a value of <1 or >13
        """
        self.assertRaises(AssertionError, Card, 0, Suit.DIAMOND)
        self.assertRaises(AssertionError, Card, 14, Suit.DIAMOND)


if __name__ == '__main__':
    unittest.main()
