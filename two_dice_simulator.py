# two_dice_simulator.py
# Simulates 2 dice being rolled and outputs probablillity
# By Tony Huang
# Version 0.1
import random


def roll():
    """Rolls 2 dice and returns the total value"""
    return (random.randint(1, 6) + random.randint(1, 6))


def main():
    """ Keeps track of all the roll results"""
    results = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
    for i in range(1000):
        value = roll()
        for x in range(13):
            if x == value:
                results[x] = results[x] + 1
    print(results)


main()
