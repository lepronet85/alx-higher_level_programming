#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string

    new_string = ""
    for i in range(len(string)):
        if i != n:
            new_string += string[i]
    return new_string
