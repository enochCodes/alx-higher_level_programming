#!/usr/bin/python3
'''1-my_list.py
'''


class MyList(list):
    ''' This class inherits from list() '''
    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
