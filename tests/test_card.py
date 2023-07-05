
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
        cards = [Card(1, Suit.DIAMOND), Card(13, Suit.CLUB), Card(5, Suit.HEART)]
        self.assertEqual("[AD, KC, 5H]", str(cards))

    def test_equality(self):
        self.assertEqual(Card(2, Suit.SPADE), Card(2, Suit.SPADE))

    def test_to_full_name(self):
        self.assertEqual("Diamond", Suit.DIAMOND.to_full_name())
        self.assertEqual("Heart", Suit.HEART.to_full_name())
        self.assertEqual("Club", Suit.CLUB.to_full_name())
        self.assertEqual("Spade", Suit.SPADE.to_full_name())


if __name__ == '__main__':
    unittest.main()
