import collections

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit[0]}"

def evaluate_5_cards(cards):
    ranks = sorted([c.rank for c in cards], reverse=True)
    suits = [c.suit for c in cards]
    counts = collections.Counter(ranks)
    
    is_flush = len(set(suits)) == 1
    
    is_straight = False
    if len(counts) == 5 and ranks[0] - ranks[4] == 4:
        is_straight = True
    elif ranks == [14, 5, 4, 3, 2]:
        is_straight = True
        ranks = [5, 4, 3, 2, 14]

    counts_sorted = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    pattern = [x[1] for x in counts_sorted]
    ranked_vals = [x[0] for x in counts_sorted]

    if is_flush:
        return (5, ranks), "Flush"
    if is_straight:
        return (4, ranks), "Straight"
    if pattern == [3, 1, 1]:
        return (3, ranked_vals), "Three of a kind"
    if pattern == [2, 2, 1]:
        return (2, ranked_vals), "Two pair"
    if pattern == [2, 1, 1, 1]:
        return (1, ranked_vals), "One pair"
    
    return (0, ranks), "High card"