#!/usr/bin/python3
def best_score(a_dictionary):
    result = None
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > result:
                result = a_dictionary[key]
                winner = key
        return the_winner
