#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import math
    if len(sys.argv) == 1:
        print("0")
    else:
        args_num = [int(arg) for arg in sys.argv[1:]]
        sum_args = sum(args_num)
        print("{:d}".format(sum_args))
