#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "":
        result = (len(sentence), sentence[0])
        return result
    return 0, None
