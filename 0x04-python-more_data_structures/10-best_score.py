#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    l_keys = list(a_dictionary.keys())
    l_vals = list(a_dictionary.values())
    score = l_vals[0]
    scorer = l_keys[0]

    for i, j in zip(l_keys, l_vals):
        if j > score:
            score = j
            scorer = i
    return scorer
