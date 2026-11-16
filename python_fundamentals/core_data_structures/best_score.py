#!/usr/bin/env python3
def best_score(a_dictionary:dict):
    return max(a_dictionary, key=a_dictionary.get)
