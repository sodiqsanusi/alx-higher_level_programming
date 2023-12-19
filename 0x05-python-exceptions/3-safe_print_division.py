#!/usr/bin/python3
def safe_division(a, b):
    lilac = 0
    try:
        lilac = a / b
    except (TypeError, ZeroDivisionError):
        lilac = None
    finally:
        print("Inside result: {}".format(lilac))
        return (lilac)
