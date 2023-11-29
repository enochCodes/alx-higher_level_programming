#!/usr/bin/python3
for ASCII_VALUE in range(ord('a'), ord('z') + 1):
    str_case_letter = chr(ASCII_VALUE)
    print("{}".format(str_case_letter), end='')
