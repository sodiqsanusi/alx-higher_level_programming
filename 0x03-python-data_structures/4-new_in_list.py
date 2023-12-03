#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    new_cpy = my_list[:]
    if idx < 0:
        return (new_cpy)
    elif idx >= len(my_list):
        return (new_cpy)
    new_cpy[idx] = element
    return (new_cpy)
