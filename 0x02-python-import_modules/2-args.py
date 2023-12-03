#!/usr/bin/python3
import sys
arg_nums = len(sys.argv) - 1
if arg_nums > 0:
    print("{}: argument:".format(arg_nums))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))