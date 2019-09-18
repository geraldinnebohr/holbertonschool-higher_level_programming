#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        tuple_return = (length, None)
        return tuple_return
    tuple_return = (length, sentence[0])
    return tuple_return
