#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
