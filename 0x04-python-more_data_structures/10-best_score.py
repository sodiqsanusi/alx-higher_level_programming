#!/usr/bin/python3
def best_score(a_dictionary):
    final = None
    for key, value in a_dictionary.items():
        if final is None:
            final = key
        if value > a_dictionary[final]:
            final = key
    return (final)
