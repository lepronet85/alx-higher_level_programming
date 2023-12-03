#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    if not my_list:
        pass
    for j in range(len(my_list)):
        print("{:d}".format(my_list[i]))
        i -= 1
