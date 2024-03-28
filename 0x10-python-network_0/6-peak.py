#!/usr/bin/python3
"""
This function identifies a peak in an unsorted list of integers.
"""


def find_peak(list_of_integers):
    """
    Determine and return a peak value from a list of unsorted integers.
    """
    # Check for empty list, return None if true
    if len(list_of_integers) == 0:
        return None
    # If list contains only one element, return that element as the peak
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    # For a list with two elements, return the maximum value as the peak
    if len(list_of_integers) == 2:
        return max(list_of_integers)

    # Calculate the middle index of the list
    mid = int(len(list_of_integers) / 2)
    # Assign the middle element to the variable 'peak'
    peak = list_of_integers[mid]
    # Check if the middle element is a peak by comparing it with its neighbors
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    # If the middle element is not a peak and is less than its left neighbor,
    # recursively search the left half of the list for a peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    # If the middle element is not a peak and is greater than or
    # equal to its left neighbor,
    # recursively search the right half of the list for a peak.
    else:
        return find_peak(list_of_integers[mid + 1:])
