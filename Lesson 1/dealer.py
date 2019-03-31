from poker_game import poker
import random  # this will be a useful library for shuffling

"""This builds a deck of 52 cards"""


MYDECK = [r + s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=MYDECK):
    random.shuffle(deck)
    return [deck[i * n:(i + 1) * n] for i in range(numhands)]

# print(deal(2))


def main():
    hands = deal(3, n=5, deck=MYDECK)
    print(hands)
    print("Winner hand: " + str(poker(hands)))


if __name__ == "__main__":
    main()
