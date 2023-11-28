#!/usr/bin/python3
for word in range(ord('a'), ord('z') + 1):
    if ((word == ord('q')) or (word == ord('e'))):
        continue
    print('{:c}'.format(word), end="")
