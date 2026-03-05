class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit[0]}"

def evaluate_5_cards(cards):
    ranks = sorted([c.rank for c in cards], reverse=True)
    return (0, ranks), "High card"