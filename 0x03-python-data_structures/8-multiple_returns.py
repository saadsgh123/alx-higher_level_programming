#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "" or sentence is not None:
        result = (len(sentence), sentence[0])
        return result
    else:
        return len(sentence), None
