#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lilac = sys.argv[1:]
    violet = len(lilac)
    if violet == 0:
        print("0 arguments.")
    elif violet == 1:
        print("1 argument:")
    else:
        print(f"{violet:d} arguments:")
    print(lilac)
