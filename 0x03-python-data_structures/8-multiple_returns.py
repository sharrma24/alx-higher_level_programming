#!/usr/bin/python3
def multiple_returns(sentence):
    def multiple_returns(sentence):
    result_tuple = ()
    if len(sentence) == 0:
        result_tuple = 0," None"
    else:
        result_tuple = len(sentence), sentence[0]
    return result_tuple
