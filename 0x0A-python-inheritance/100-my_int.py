#!/usr/bin/python3
"""100-my_int.py
"""


class MyInt(int):
    """myint inerted from int"""
    def __new__(cls, value):
        return super().__new__(cls, value)

    def __eq__(self, other):
        """eqality inverted"""
        return super().__ne__(other)

    def __ne__(self, other):
        """inequality inverted"""
        return super().__eq__(other)
