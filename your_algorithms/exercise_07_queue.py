"""
7.7.3 우선순위 큐와 힙

heapq 모듈을 사용하여 시퀀스에서 N개의 가장 큰 항목과 가장 작은 항목을 찾아보자.
"""

import doctest
import heapq


def find_smallest_with_list(seq):
    """
    >>> find_smallest_with_list([1,2,3,4,5])
    1
    >>> find_smallest_with_list([5,4,3,2,0])
    0
    """
    return min(seq)


def find_smallest_with_heap(seq):
    """
    >>> find_smallest_with_heap([1,2,3,4,5])
    1
    >>> find_smallest_with_heap([5,4,2,0])
    0
    """
    heapq.heapify(seq)
    return heapq.heappop(seq)


def find_n_smallest_items_with_list(seq, n):
    """
    >>> find_n_smallest_items_with_list([5,4,3,2,1], 1)
    [1]
    """
    seq.sort()
    return seq[:n]


def find_n_smallest_items_with_heapq(seq, n):
    """
    >>> find_n_smallest_items_with_heapq([1,2,3,4,5], 1)
    [1]
    >>> find_n_smallest_items_with_heapq([5,4,3,2,1], 1)
    [1]
    >>> find_n_smallest_items_with_heapq([5,4,3,2,1], 2)
    [1, 2]
    >>> find_n_smallest_items_with_heapq([1,2,3,4,5], 2)
    [1, 2]
    """
    return heapq.nsmallest(n, seq)


def find_largest_with_list(seq):
    """
    >>> find_largest_with_list([1,2,3,4])
    4
    >>> find_largest_with_list([4,3,2,1])
    4
    """
    return max(seq)


def find_largest_with_heapq(seq):
    """
    >>> find_largest_with_heapq([1,2,3,4,5])
    5
    >>> find_largest_with_heapq([6,4,3,2])
    6
    """
    h = [(-item, item) for item in seq]
    heapq.heapify(h)
    return heapq.heappop(h)[1]


def find_n_largest_items_with_list(seq, n):
    """
    >>> find_n_largest_items_with_list([1,2,3,4, 5], 1)
    [5]
    >>> find_n_largest_items_with_list([5,4,3,2,1], 1)
    [5]
    >>> find_n_largest_items_with_list([1,2,3,4,5], 2)
    [5, 4]
    >>> find_n_largest_items_with_list([5,4,3,2,1], 2)
    [5, 4]
    """
    seq.sort(reverse=True)
    return seq[:n]


def find_n_largest_items_with_heapq(seq, n):
    """
    >>> find_n_largest_items_with_heapq([1,2,3,4,5], 1)
    [5]
    >>> find_n_largest_items_with_heapq([5,4,3,2,1], 1)
    [5]
    >>> find_n_largest_items_with_heapq([5,4,3,2,1], 2)
    [5, 4]
    >>> find_n_largest_items_with_heapq([1,2,3,4,5], 2)
    [5, 4]
    """
    return heapq.nlargest(n, seq)


if __name__ == "__main__":
    doctest.testmod()