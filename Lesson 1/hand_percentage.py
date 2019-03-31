from poker_game import *
from dealer import *

HAND_NAMES = ['Straight Flush', '4 Kind', 'Full House',
              'Flush', 'Straight', '3 Kind', '2 Pair',
              'Pair', 'High Card']

def hand_percentages(n=700*1000):
    """"Sample n random hands and print a table
    of percentages for each type of hand"""
    counts = [0]*9

    for i in range((int)(n/10)):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking]+=1

    for i in reversed(range(9)):
        print("%14s: %6.3f %%" %(HAND_NAMES[::-1][i], 100.*counts[i]/n))

def main():
    hand_percentages()

if __name__=='__main__':
    main()