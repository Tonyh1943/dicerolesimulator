# two_dice_simulator.py
# Simulates 2 dice being rolled and outputs probablillity
# By Tony Huang
# Version 1
import random


def roll():
    """Rolls 2 dice and returns the total value"""
    return (random.randint(1, 6) + random.randint(1, 6)) # Simulates and adds up two d6 rolls


def percentage(totals):
    """ Convert each total into percentages of all rolls"""
    percentages = {}
    for i in range(2, 13):
        percentages[i] = (float(totals[i])/10)
    return percentages


def output(simulation_percentages):
    """Outputs the percentages and expected percentages"""
    EXPECTED_PERCENTAGES = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}

    #Output results in table format
    print("Total | Expected Value |Actual Value")
    for i in range (2, 13):
        print("{}     |{}             |{}   ".format(i,  EXPECTED_PERCENTAGES[i], simulation_percentages[i]))


def loop():
    """ Keeps track of all the roll results"""
    results = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for i in range(1000):  # Repeats the dice roll 1000 times
        value = roll()

        # Every time the dice roll occurs, find out which key in the results dictionary it corresponds with and add it to the tally
        for x in range(13):
            if x == value:  # Checks if result equals a given key
                results[x] = results[x] + 1
    output(percentage(results))


def main():
    while True:
        choice = str(input("What would you like to do?: \n 1. Roll and Display Table \n 2. Exit \n "))
        if choice == "1":
            loop()
        elif choice == "2":
            break
        else:
            print("Invalid input, enter 1 or 2")


main()
