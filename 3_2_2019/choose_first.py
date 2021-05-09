import random


def choose_first():
    flip = random.randint(0, 100)
    if flip%2 == 0:
        return 'Player 1'
    return 'Player 2'
