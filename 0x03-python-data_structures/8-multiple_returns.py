#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
    length = len(sentence)
    tuple_return = (length, sentence[0])
    return tuple_return
