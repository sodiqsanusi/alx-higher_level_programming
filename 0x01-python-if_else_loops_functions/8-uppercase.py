#!/usr/bin/python3
def uppercase(str):
    for word in str:
        asc = ord(word)
        if (asc > 96) and (asc < 123):
            asc = asc - 32
        print('{:c}'.format(asc), end='')
    print('{:c}'.format(10), end='')
