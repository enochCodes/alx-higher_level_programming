#!/usr/bin/python3
"""
    prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        text must be a string, otherwise raise a TypeError exception with the message text must be a string
        There should be no space at the beginning or at the end of each printed line
        You are not allowed to import any module
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        punctuations = '.', '?', ':'
        for char in text:
            print(char, end='')
            if char in punctuations:
                print("\n\n", end='')
