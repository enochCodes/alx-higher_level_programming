def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            count += 1
    except IndexError:
        pass  # Continue execution if index out of range
    finally:
        print()  # Move to the next line after printing all elements
    return count
