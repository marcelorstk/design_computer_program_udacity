from poker_game import *

def test():
    """Test cases for fuction in poker program"""
    # Split will create a list => [6c, ...]
    sf = "6C 7C 8C 9C TC".split()   # straight flush
    fk = "9D 9H 9S 9C 7D".split()   # four of a kind
    fh = "TD TC TH 7C 7D".split()   # full house
    al = "AC 2D 4H 3D 5S".split()   # Ace-Low Straight
    fkranks = card_ranks(fk)

    # Asserts cards ranks is doing well (ordered list of numbers)
    assert card_ranks(sf) == [10,9,8,7,6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]
    assert card_ranks(['AC', '3D', '4S', 'KH']) == [14,13,4,3]

    # Check por types of hands
    assert flush(sf) == True
    assert flush(fh) == False
    assert straight(card_ranks(sf)) == True
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert kind(3, card_ranks(fh)) == 10
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert straight(card_ranks(al)) == True

    # Test of the function hand rank
    assert hand_rank(sf) == (8,10)
    assert hand_rank(fk) == (7,9,7)
    assert hand_rank(fh) == (6, 10, 7)


    # Check for poker function
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    # Check for 1 and 100 players
    assert poker([fk]) == [fk]
    assert poker([sf] * 30 + [fk] * 40 + [fh] * 30) == [sf] *30

    return 'test pass'

print(test())