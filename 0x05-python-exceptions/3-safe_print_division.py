#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("\nInside result: {}".format(result))
    finally:
        if result is not None:
            print("\nInside result: {:.1f}".format(result))
    return result
