#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_count = 0
    try:
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    print_count += 1
            except IndexError:
                break
    except (TypeError, IndexError):
        pass
    finally:
        print()
    return (print_count)
