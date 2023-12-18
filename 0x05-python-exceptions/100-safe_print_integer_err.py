#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as ve:
        import sys
        sys.stderr.write("Exception: {}\n".format(ve))
        return False
    else:
        return True
