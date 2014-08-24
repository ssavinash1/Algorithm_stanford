# -*- coding: utf-8 -*-

from src.merge_sort import merge_sort
from src.quick_sort import partition


def split_chunks(arr, size):
    """ Splits the input array into subarrays of given size.

    Params:
        arr: input list to be split.
        size: the size of the smaller arrays.

    Returns:
        list of lists of the indicated size with elements from arr.
    """
    output = []
    for i in range(0, len(arr), size):
        output.append(arr[i:i+size])
    return output

def pick_middle(arr):
    """ Picks the middle element from an array.

    Note that the size of the array should be very small.

    Params:
        arr: list of elements.

    Returns:
        The value of the elment in the middle of the list.
    """
    arr = merge_sort(arr)
    middle = int(round(len(arr)/2))
    return arr[middle]

def deterministic_pick_pivot(arr):
    """ Pick the best pivot possible in a deterministic manner.

    Use the median of medians method.

    Params:
        arr: list of elements

    Returns:
        A value representing the picked pivot.
    """
    if len(arr) < 5:
        return pick_middle(arr)

    chunks = split_chunks(arr, 5)
    medians = [pick_middle(chunk) for chunk in chunks]
    return deterministic_pick_pivot(medians)

def deterministic_selection(arr, n, i):
    """ Computes the ith element from a non-sorted array in a
    deterministic way, ie. non-randomised.

    The ideea is to always compute the best pivot by using the median of medians
    recursive call which runs in logarithmic time.

    Params:
        arr: list of elements
        n: size of the arr
        i: which order statistic to pick from the array.

    Returns:
        The value on the ith position in the sorter arr.
    """
    pos = deterministic_pick_pivot(arr)
    arr[pos], arr[0] = arr[0], arr[pos]

    pos = partition(arr, 0, len(arr) - 1)

    if pos == i:
        return arr[pos]
    elif pos > i:
        return randomized_selection(arr[0:pos], (pos - 1), i)
    else:
        return randomized_selection(arr[pos+1:], (n - pos - 1), (i - pos - 1))