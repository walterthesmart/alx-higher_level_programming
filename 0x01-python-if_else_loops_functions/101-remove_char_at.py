#!/usr/bin/python3
# function that creates a copy of the string,
# removing the character at the position n
# created by bright

def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
