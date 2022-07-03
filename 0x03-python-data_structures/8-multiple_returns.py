#!/usr/bin/bash
def multiple_returns(sentence):
    str_len = len(sentence)
    if len(sentence) <= 0:
        first_char = "None"
    else:
        first_char = sentence[0]
    return (str_len, first_char)
