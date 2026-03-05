import unittest
from poker import Card, evaluate_5_cards

class TestPoker(unittest.TestCase):
    def test_high_card(self):
        cards = [Card(14, 'Hearts'), Card(10, 'Spades'), Card(7, 'Clubs'), Card(4, 'Diamonds'), Card(2, 'Hearts')]
        score, name = evaluate_5_cards(cards)
        self.assertEqual(name, "High card")
        self.assertEqual(score[0], 0)

if __name__ == '__main__':
    unittest.main()