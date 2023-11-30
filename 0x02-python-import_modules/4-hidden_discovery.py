#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lilac = dir(hidden_4)
    for word in lilac:
        if word[0] == '_' and word[1] == '_':
            continue
        print(word)
