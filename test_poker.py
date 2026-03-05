import unittest
from poker import Card, evaluate_5_cards

class TestPoker(unittest.TestCase):
    def test_high_card(self):
        cards = [Card(14, 'Hearts'), Card(10, 'Spades'), Card(7, 'Clubs'), Card(4, 'Diamonds'), Card(2, 'Hearts')]
        score, name = evaluate_5_cards(cards)
        self.assertEqual(name, "High card")
        self.assertEqual(score[0], 0)

    def test_one_pair(self):
        cards = [Card(10, 'Hearts'), Card(10, 'Spades'), Card(7, 'Clubs'), Card(4, 'Diamonds'), Card(2, 'Hearts')]
        score, name = evaluate_5_cards(cards)
        self.assertEqual(name, "One pair")
        self.assertEqual(score[0], 1)

    def test_two_pair(self):
        cards = [Card(10, 'Hearts'), Card(10, 'Spades'), Card(7, 'Clubs'), Card(7, 'Diamonds'), Card(2, 'Hearts')]
        score, name = evaluate_5_cards(cards)
        self.assertEqual(name, "Two pair")
        self.assertEqual(score[0], 2)

    def test_three_of_a_kind(self):
        cards = [Card(10, 'Hearts'), Card(10, 'Spades'), Card(10, 'Clubs'), Card(4, 'Diamonds'), Card(2, 'Hearts')]
        score, name = evaluate_5_cards(cards)
        self.assertEqual(name, "Three of a kind")
        self.assertEqual(score[0], 3)

if __name__ == '__main__':
    unittest.main()