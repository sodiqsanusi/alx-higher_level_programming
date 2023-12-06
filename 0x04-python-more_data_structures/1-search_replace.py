#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def filter(x):
        if x == search:
            return (replace)
        return (x)
    final = list(map(filter, my_list))
    return (final)
