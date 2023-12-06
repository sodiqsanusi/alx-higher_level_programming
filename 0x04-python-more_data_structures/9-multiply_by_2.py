#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    final = {}
    for key in a_dictionary:
        final[key] = a_dictionary[key] * 2
    return (final)
