#!/usr/bin/python3
# function that retrieves an element from a list like in c
# created by Walter


def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return 'None'
    else:
        return my_list[idx]
