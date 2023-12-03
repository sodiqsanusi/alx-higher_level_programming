#!/usr/bin/python3
def no_c(my_string):
    sort_string = []
    for char in my_string:
        if (char == 'c') or (char == 'C'):
            continue
        sort_string.append(char)
    final_str = "".join(sort_string)
    return (final_str)
