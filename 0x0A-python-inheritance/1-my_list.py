#!/usr/bin/python3
'''1-my_list.py
'''


class MyList(list):
    def print_sorted(self):
        """Print the list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
