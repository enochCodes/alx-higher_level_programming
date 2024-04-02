#!/usr/bin/python3
def safe_print_integer(value):
    try:
        new_int = int(value)
        print("{:d}".format(new_int))
        return True
    except ValueError:
        return False
