#!/usr/bin/env python3
def return_evens(num_list):
    new_arr=[]
      #  new_arr=[x for x in num_list if x % 2 == 0]
        #return new_arr
    for x in num_list:
        if x % 2 == 0:
            new_arr.append(x)
    return new_arr
    

def make_exclamation(sentence_list):
    # new_sentence_list = [sentence + '!' for sentence in sentence_list]
    # return new_sentence_list
    new_sentence_list = []
    for sentence in sentence_list:
        new_sentence = sentence + "!"
        new_sentence_list.append(new_sentence)
    return new_sentence_list