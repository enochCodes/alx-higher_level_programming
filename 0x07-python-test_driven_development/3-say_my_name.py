#!/usr/bin/python3
"""
    print the user name
"""


def say_my_name(first_name, last_name=""):
    """
        the function print the name inter as argumet

        args:
            first_name
            last_name
        if the arguments are mot str reaise type Error
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("my name is {} {}".format(first_name, last_name))
