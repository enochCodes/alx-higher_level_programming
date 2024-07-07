#!/usr/bin/python3
"""
Peak finding in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Find a peak element in a list of unsorted integers."""
    if not list_of_integers:
        return None

    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)


def binary_search_peak(arr, low, high):
    """Helper function to perform binary search for peak finding."""
    mid = (low + high) // 2

    # Check if mid element is a peak
    if (
        (mid == 0 or arr[mid] >= arr[mid - 1]) and
        (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1])
    ):
        return arr[mid]
    # If the left neighbor is greater, search in the left half
    elif mid > 0 and arr[mid] < arr[mid - 1]:
        return binary_search_peak(arr, low, mid - 1)
    # If the right neighbor is greater, search in the right half
    else:
        return binary_search_peak(arr, mid + 1, high)
