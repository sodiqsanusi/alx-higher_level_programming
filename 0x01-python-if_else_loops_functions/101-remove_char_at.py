#!/usr/bin/python3
def remove_char_at(str, n):
    lilac = 0
    new_string = ""
    for char in str:
        if lilac == n:
            lilac += 1
            continue
        new_string = new_string + char
        lilac += 1
    return (new_string)
