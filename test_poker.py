import unittest
from poker import Card, evaluate_5_cards, best_hand

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

    def test_straight(self):
        cards = [Card(9, 'Hearts'), Card(8, 'Spades'), Card(7, 'Clubs'), Card(6, 'Diamonds'), Card(5, 'Hearts')]
        score, name = evaluate_5_cards(cards)
        self.assertEqual(name, "Straight")
        self.assertEqual(score[0], 4)

    def test_straight_ace_low(self):
        cards = [Card(14, 'Hearts'), Card(5, 'Spades'), Card(4, 'Clubs'), Card(3, 'Diamonds'), Card(2, 'Hearts')]
        score, name = evaluate_5_cards(cards)
        self.assertEqual(name, "Straight")
        self.assertEqual(score[1], [5, 4, 3, 2, 14])

    def test_flush(self):
        cards = [Card(10, 'Hearts'), Card(8, 'Hearts'), Card(7, 'Hearts'), Card(4, 'Hearts'), Card(2, 'Hearts')]
        score, name = evaluate_5_cards(cards)
        self.assertEqual(name, "Flush")
        self.assertEqual(score[0], 5)

    def test_full_house(self):
        cards = [Card(10, 'Hearts'), Card(10, 'Spades'), Card(10, 'Clubs'), Card(4, 'Diamonds'), Card(4, 'Hearts')]
        score, name = evaluate_5_cards(cards)
        self.assertEqual(name, "Full house")
        self.assertEqual(score[0], 6)

    def test_four_of_a_kind(self):
        cards = [Card(10, 'Hearts'), Card(10, 'Spades'), Card(10, 'Clubs'), Card(10, 'Diamonds'), Card(2, 'Hearts')]
        score, name = evaluate_5_cards(cards)
        self.assertEqual(name, "Four of a kind")
        self.assertEqual(score[0], 7)

    def test_straight_flush(self):
        cards = [Card(9, 'Hearts'), Card(8, 'Hearts'), Card(7, 'Hearts'), Card(6, 'Hearts'), Card(5, 'Hearts')]
        score, name = evaluate_5_cards(cards)
        self.assertEqual(name, "Straight flush")
        self.assertEqual(score[0], 8)

    def test_best_hand_selection(self):
        board = [Card(14, 'Hearts'), Card(2, 'Spades'), Card(3, 'Clubs'), Card(4, 'Diamonds'), Card(9, 'Hearts')]
        hole = [Card(5, 'Clubs'), Card(13, 'Spades')]
        score, cards, name = best_hand(hole, board)
        self.assertEqual(name, "Straight")

if __name__ == '__main__':
    unittest.main()