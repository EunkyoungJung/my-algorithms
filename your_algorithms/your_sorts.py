"""
Bubble Sort
"""

import doctest


def bubble_sort(seq):
    """
    >>> bubble_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    """
    length = len(seq) - 1
    for num in range(length, 0, -1):
        for i in range(num):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq


def selection_sort(seq):
    """
    >>> selection_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    """
    length = len(seq)
    for i in range(length-1):
        min_idx = i
        for j in range(i+1, length):
            if seq[min_idx] > seq[j]:
                min_idx = j
        seq[i], seq[min_idx] = seq[min_idx], seq[i]
    return seq


if __name__ == "__main__":
    doctest.testmod()