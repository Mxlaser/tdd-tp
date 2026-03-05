import collections
import itertools

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

    if is_straight and is_flush:
        return (8, ranks), "Straight flush"
    if pattern == [4, 1]:
        return (7, ranked_vals), "Four of a kind"
    if pattern == [3, 2]:
        return (6, ranked_vals), "Full house"
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

def best_hand(hole_cards, board):
    all_cards = hole_cards + board
    best_score = (-1, [])
    best_cards = []
    best_name = ""
    
    for combo in itertools.combinations(all_cards, 5):
        score, name = evaluate_5_cards(combo)
        if score > best_score:
            best_score = score
            best_cards = list(combo)
            best_name = name
            
    counts = collections.Counter(c.rank for c in best_cards)
    is_ace_low = set(c.rank for c in best_cards) == {14, 2, 3, 4, 5}
    
    if is_ace_low and best_name in ["Straight", "Straight flush"]:
        best_cards.sort(key=lambda c: c.rank if c.rank != 14 else 1, reverse=True)
    else:
        best_cards.sort(key=lambda c: (counts[c.rank], c.rank), reverse=True)
        
    return best_score, best_cards, best_name

def compare_players(players_holes, board):
    best_scores = []
    for hole in players_holes:
        score, cards, name = best_hand(hole, board)
        best_scores.append(score)
        
    max_score = max(best_scores)
    winners = [i for i, score in enumerate(best_scores) if score == max_score]
    return winners