#!/usr/bin/env python3
def return_evens(num_list):
    nums = []
    for x in num_list:
        if x % 2 == 0:
            nums.append(x)
    return nums

    

def make_exclamation(sentence_list):
    new_list = []
    for sentence in sentence_list:
        new_list.append(sentence + "!")
    return new_list
    
            