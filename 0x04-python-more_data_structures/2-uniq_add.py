#!/usr/bin/python3
def uniq_add(my_list=[]):
    track_list = []
    result = 0
    for elem in my_list:
        if elem not in new_list:
            result += elem
            track_list.append(elem)
    return result
