#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("\nInside result: {}".format(result))
    return result
