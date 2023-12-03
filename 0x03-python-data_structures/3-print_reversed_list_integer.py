#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list)
    while idx > 0:
        print("{:d}".format(my_list[idx - 1]))
        idx -= 1
