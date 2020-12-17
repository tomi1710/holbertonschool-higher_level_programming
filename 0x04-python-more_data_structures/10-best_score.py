#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        mx = -10000000000

        for i in a_dictionary:
            if (mx < a_dictionary[i]):
                mx = a_dictionary[i]

        return (mx)
    else:
        return (None)
