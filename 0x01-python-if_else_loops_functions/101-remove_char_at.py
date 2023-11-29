#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string  # If n is out of range, return the original string

    new_string = ""
    for i in range(len(string)):
        if i != n:
            new_string += string[i]  # Append all characters except the one at position n
    return new_string
