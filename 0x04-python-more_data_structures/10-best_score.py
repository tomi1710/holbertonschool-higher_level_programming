#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        mx = 0
        for i in a_dictionary:
            if (mx < a_dictionary[i]):
                mx = a_dictionary[i]
                a = i

        return (a)
    else:
        return (None)
