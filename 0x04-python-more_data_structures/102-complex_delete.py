#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, pair in a_dictionary.items():
        if (pair == value):
            del a_dictionary[key]
    return (a_dictionary)
