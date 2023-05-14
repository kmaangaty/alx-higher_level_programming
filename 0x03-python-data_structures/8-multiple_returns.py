#!/usr/bin/python3
def multiple_returns(sentence):
    sl = len(sentence)
    if sl >= 1:
        res = (len(sentence), sentence[:1])
        return res
    else:
        return (0, None)
