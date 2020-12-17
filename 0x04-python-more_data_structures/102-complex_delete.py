#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dic = {}
    for i in a_dictionary:
        if (a_dictionary[i] != value):
            a_dic[i] = a_dictionary[i]
    a_dictionary.clear()
    for i in a_dic:
        a_dictionary[i] = a_dic[i]
    return (a_dictionary)
