"""
Bubble Sort
"""

import doctest
from collections import defaultdict


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


def insertion_sort(seq):
    """
    >>> insertion_sort([5, 3, 2, 4])
    [2, 3, 4, 5]
    """
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq


def insertion_sort_rec(seq, i=None):
    if i is None:
        i = len(seq) - 1
    if i == 0:
        return i

    insertion_sort(seq, i)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq


def gnome_sort(seq):
    """
    >>> gnome_sort([5, 3, 2, 4])
    [2, 3, 4, 5]
    """
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
    return seq


def count_sort_dict(seq):
    """
    >>> count_sort_dict([1, 1, 5, 5, 3, 3, 2, 2])
    [1, 1, 2, 2, 3, 3, 5, 5]
    """
    b, c = [], defaultdict(list)
    for x in seq:
        c[x].append(x)
    for k in range(min(c), max(c) + 1):
        b.extend(c[k])
    return b


def merge_sort(seq):
    """
    리스트를 반으로 나누어 정렬되지 않은 리스트를 만든다.
    정렬되지 않은 두 리스트의 크기가 1이 될 때까지, 계속 리스트를 반으로 나누어
    병렬 정렬 알고리즘을 호출하여 리스트를 정렬하고 병합한다.
    >>> merge_sort([5, 3, 2, 4])
    [2, 3, 4, 5]
    """
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]

    # seq에 하나의 원소만 남을 때 까지 merge_sort 호출
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    # seq에 원소가 하나 일 때 아래의 로직 실행
    res = []
    while left and right:
        # 큰것부터 삽입
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse() # 오름차순으로 들어가있는 갑들을 반대로 정렬(결론적으로는 오름차순으로 정렬된 효과)
    return(left or right) + res


if __name__ == "__main__":
    doctest.testmod()