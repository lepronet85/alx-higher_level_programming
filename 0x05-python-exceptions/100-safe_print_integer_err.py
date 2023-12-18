#!/usr/bin/python3

def safe_print_integer_err(value):
    integer_value = int(value)
    try:
        print("{:d}".format(integer_value))
    except ValueError as ve:
        import sys
        print("Exception: {}".format(ve), file=sys.stderr)
        return False
    else:
        return True
