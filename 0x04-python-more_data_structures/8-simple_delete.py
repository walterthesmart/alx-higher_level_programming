#!/usr/bin/python3
# function that deletes a key in a dictionary
# created by Walter


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
