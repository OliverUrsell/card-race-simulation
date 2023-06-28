
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


if __name__ == '__main__':
    unittest.main()
