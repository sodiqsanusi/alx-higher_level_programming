#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    lilac = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            lilac += 1
        except (TypeError, ValueError):
            i += 1
            continue
    print("")
    return (lilac)
