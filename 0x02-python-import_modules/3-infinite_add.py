#!/usr/bin/python3
from sys import argv


def infinite_add():
    total = 0
    for arg in argv[1:]:
        total += int(arg)
    print(total)


if __name__ == "__main__":
    infinite_add()
