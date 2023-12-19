#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        lilac = fct(*args)
        return (lilac)
    except Exception as errs:
        sys.stderr.write("Exception: {}\n".format(errs))
        return (None)
