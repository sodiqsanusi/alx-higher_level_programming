#!/usr/bin/python3
def weight_average(my_list=[]):
    final = 0
    total = 0
    for x, y in my_list:
        final += x * y
        total += y
    if total == 0:
        return (0)
    return (final / total)
