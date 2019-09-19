#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_val = max(key for key, value in a_dictionary.items())
    return max_val
