#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_to_set = set(my_list)
    final = 0
    for x in list_to_set:
        final += x
    return (final)
