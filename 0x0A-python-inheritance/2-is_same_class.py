#!/usr/bin/python3
'''2-is_same_class.py
'''


def is_same_class(obj, a_class):
    """check the obj is the same with the class inhiretes"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
