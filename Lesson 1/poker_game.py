from typing import Any


def poker(hands):
    """"Return a list of winning hand: poker([hand,...]) => [hand]"""
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # print(hand_rank(max(iterable,key=hand_rank)))
    return [hand for hand in iterable if hand_rank(hand) == hand_rank(max(iterable, key=hand_rank))]


def hand_rank(hand):
    """"Return a velue indicating the ranking of a hand"""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):  # straighflush
        return (8, max(ranks))
    # we`ll have to think about how kind return values since here we want a bool
    # and here a number e.g 4,4,4,4,3 --> (7, 4, 1)
    elif kind(4, ranks):  # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):  # Full House
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):  # flush
        return (5, ranks)
    elif straight(ranks):  # straight
        return (4, max(ranks))
    elif kind(3, ranks):  # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):  # 2 pairs
        return (2, two_pair(ranks), kind(1, ranks))
    elif kind(2, ranks):  # pair
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(hand):
    """"Return a list of the ranks, sorted with higher first"""
    # Note: A can be either 1 or 14
    ranks = ['0123456789TJQKA'.index(r) for r, s in hand]  # type: list
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


"""""Now the types of hands"""


def flush(hand):
    """"Return True if all the cards have the same suit."""
    suits = {s for r, s in hand}
    if (len(suits) == 1):
        return True
    else:
        return False


def straight(ranks):
    """"Return True if the ordered ranks form a 5-card straight."""
    # Since ranks are already ordered
    if (ranks[0] - ranks[-1]) == 4 and len(set(ranks)) == 5:
        return True
    else:
        return False



# Pay attention to his method, it`s way easier
# Peter's function, way better than the one i did
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    if kind(2, ranks) != None and kind(2, ranks[::-1]) != None and kind(2, ranks) != kind(2, ranks[::-1]):
        return (kind(2, ranks), kind(2, ranks[::-1]))
    return None

