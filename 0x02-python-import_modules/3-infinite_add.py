#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lilac = sys.argv[1:]
    result = 0
    for word in lilac:
        result += int(word)
    print(result)
