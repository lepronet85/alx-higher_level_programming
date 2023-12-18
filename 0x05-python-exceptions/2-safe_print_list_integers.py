#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    try:
        for item in my_list[:x]:
            if isinstance(item, int):
                print("{:d}".format(item), end='')
                printed_integers += 1
        print()
    except (ValueError, TypeError):
        pass
    return printed_integers
