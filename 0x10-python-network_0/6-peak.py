#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """find a peak in a list"""
    if list_of_integers:
        var = list_of_integers[0]
        for count in range(1, len(list_of_integers) - 1):
            if list_of_integers[count] > list_of_integers[count - 1] and list_of_integers[count] > list_of_integers[count + 1]:
                var = list_of_integers[count]
        return var
    else:
        return None
    
    
