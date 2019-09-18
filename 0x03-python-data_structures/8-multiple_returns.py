#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        sentence[0] = None
    length = len(sentence)
    tuple_return = (length, sentence[0])
    return tuple_return
