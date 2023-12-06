#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set_1 = set_1.difference(set_2)
    diff_set_2 = set_2.difference(set_1)
    only_diff_set = diff_set_1.union(diff_set_2)

    return only_diff_set
