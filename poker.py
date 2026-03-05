import collections

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit[0]}"

def evaluate_5_cards(cards):
    ranks = sorted([c.rank for c in cards], reverse=True)
    counts = collections.Counter(ranks)
    
    counts_sorted = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    pattern = [x[1] for x in counts_sorted]
    ranked_vals = [x[0] for x in counts_sorted]

    if pattern == [2, 1, 1, 1]:
        return (1, ranked_vals), "One pair"
    
    return (0, ranks), "High card"