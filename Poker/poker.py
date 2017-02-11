# -----------
# User Instructions
#
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands.
#
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function
#                  returns their corresponding ranks as a
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks
#                  in a hand (where the order goes from
#                  highest to lowest rank).
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will
# tell you if you are correct.

import random
import pprint

points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

mydeck = [r + s for r in '23456789TJQKA' for s in 'SHDC']

pp = pprint.PrettyPrinter(indent=4)


def deal(numhands, numcards=5, deck=mydeck):
    """shuffle the decks and deal out numhands hands with numcards"""
    random.shuffle(deck)
    return [deck[numcards * i: numcards * (i + 1)] for i in range(numhands)]

def hand_percentages(n=70*1000):
    """Sample n random hands and print distribution"""
    hand_names = ["straight flush", "four of a kind", "full house", "flush",
                  "straight", "three of a kind", "two pairs", "pair", "nothing"]
    counts = [0] * 9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
   for i in reversed(range(9)):
       print "%14s: %6.3f %%" % (hand_names[i], 100.*counts[i]/n)

d = deal(4)
pp.pprint(d)

d = deal(4)
pp.pprint(d)


def poker(hands):
    """Return a list of winning hands: poker([hand,...]) => [hand, hand]"""
    # return max(hands, key=hand_rank)
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result


def kind(param, ranks):
    pass

def two_pair(ranks):
    pass

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):  # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):  # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):  # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):  # flush
        return (5, ranks)
    elif straight(ranks):  # straight
        return (4, max(ranks))
    elif kind(3, ranks):  # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):  # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):  # 1 pair
        return (1, kind(2, ranks), ranks)
    else:  # high card
        return (0, ranks)


def card_ranks(cards):
    """Return a list of the ranks, sorted with higher first."""
    ranks = [points[r] for r, s in cards]
    # or shorter
    # ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    # exception - low straigth ace counts as 1
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight."""

    # for i in range(1, 5):
    #    if ranks[i] + 1 != ranks[i-1]:
    #        return False
    # return True
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    """Return True if all the cards have the same suit."""
    # h0 = hand[0][1]
    # for i in range(1, 5):
    #    if hand[i][1] != h0:
    #        return False
    # return True
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def test():
    """Test cases for the functions in poker program"""
    sf = "6C 7C 8C 9C TC".split()  # 8 Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # 7 Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # 6 Full House
    x = "TD JD QD KD AS".split()
    low_ace = "AC 5D 4S 3S 2D".split()

    fl = "2D 6D 9D JD KD".split()  # 5 Flush - 5 of a kind
    st = "6D 7C 8H 9C TS".split()  # 4 Straight - 5 seq.
    tk = "9D 9H 9S TC JS".split()  # 3 3 of a Kind
    tp = "9D 9H TS TC JS".split()  # 2 2 pairs
    op = "7D 7H 8S TC JS".split()  # 1 1 pair
    hc = "6D 7H TS JC AS".split()  # 0 high card J 11, Q 12, K 13, A 14

    assert straight([9, 8, 7, 6, 5])
    assert not straight([9, 8, 8, 6, 5])
    assert flush(sf)
    assert not flush(fk)
    assert not flush(x)

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert card_ranks(low_ace) == [5, 4, 3, 2, 1]

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99 * [fh]) == sf

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    assert hand_rank(fl) == (5, 13, 11, 9, 6, 2)
    assert hand_rank(st) == (4, 10)
    assert hand_rank(tk) == (3, 9, 11, 10, 9, 9, 9)
    assert hand_rank(tp) == (2, 10, 9, 11, 10, 10, 9, 9)
    assert hand_rank(op) == (1, 7, 11, 10, 8, 7, 7)
    assert hand_rank(hc) == (0, 14, 11, 10, 7, 6)

    assert card_ranks(['AC', '3D', '4S', 'KH']) == [14, 13, 4, 3]

    return 'tests pass'


test()
