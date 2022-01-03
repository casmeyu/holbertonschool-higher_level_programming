#!/usr/bin/python3

def multiple_returns(sentence):
    lsen = len(sentence)
    if lsen > 0:
        return (lsen, sentence[0])
    elif lsen == 0:
        return (lsen, None)
