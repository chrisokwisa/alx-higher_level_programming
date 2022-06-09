#!/usr/bin/python3
def best_score(a_dictionary):
    result = None
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > result:
                result = a_dictionary[key]
                winner = key
<<<<<<< HEAD
            return winner
=======
           return the_winner
>>>>>>> 68901e9cea81ebcd9f08a2986144cd178d8e1850
