

import doctest
from collections import defaultdict


# bubble sort
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


# selection sort
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


# insertion sort
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


# gnome sort
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


# count sort
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


# merge sort
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


def merge_sort_sep(seq):
    """
    두 함수로 나누어서 구현한다.
    한 함수에서는 배열을 나누고, 또 다른 함수에서는 배열을 병합한다.
    :param seq:
    :return:
    >>> merge_sort_sep([5, 3, 2, 4])
    [2, 3, 4, 5]
    """
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left = merge_sort_sep(seq[:mid])
    right = merge_sort_sep(seq[mid:])
    return merge(left, right)


def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    return result


def merge_2n(left, right):
    """
    각 두 배열은 정렬된 상태다.
    시간복잡도는 O(2n)이다.
    :param left:
    :param right:
    :return:
    >>> l1 = [1, 2, 3, 4, 5, 6, 7]
    >>> l2 = [2, 4, 5, 8]
    >>> merge_2n(l1, l2)
    [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]
    """
    if not left or not right:
        return left or right
    result = []
    while left and right:
        if left[-1] >= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    result.reverse()
    return (left or right) + result


def merge_two_arrays_inplace(l1, l2):
    """
    제자리 정렬로 구현한다.
    :param l1:
    :param l2:
    :return:
    >>> l1 = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0]
    >>> l2 = [2, 4, 5, 8]
    >>> merge_two_arrays_inplace(l1, l2)
    [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]
    """
    if not l1 or not l2:
        return l1 or l2
    p2 = len(l2) - 1
    p1 = len(l1) - len(l2) - 1
    p12 = len(l1) - 1

    # left 기준으로 정렬될 때까지
    while p2 >= 0 and p1 >= 0:
        # 오른쪽에서 하나씩 왼쪽에 정렬하여 끼워맞춤
        item_to_be_merged = l2[p2]
        # 왼쪽 배열의 마지막 원소
        item_bigger_array = l1[p1]

        if item_to_be_merged < item_bigger_array:
            l1[p12] = item_bigger_array
            p1 -= 1
        else:
            l1[p12] = item_to_be_merged
            p2 -= 1
        p12 -= 1
    return l1


def merge_files(list_files):
    """
    파일을 병합한다.
    :param list_files:
    :return:
    """
    result = []
    final = []
    for filename in list_files:
        aux = []
        with open(filename, "r") as file:
            for line in file:
                aux.append(int(line))
        result.append(aux)
    final.extend(result.pop())
    for l in result:
        final = merge(l, final)
    return final


# quick sort
"""
* pivot 값을 잘 선택하는 것은 성능의 핵심
* 피벗을 기준으로 리스트를 둘로 나눔
* 리스트의 중앙값을 피벗으로 선택하는 것은 이미 정렬된 리스트에서 가장 적한한 선택이고,
  정렬되지 않은 리스트 대부분에서도 다른 선택보다 나쁘지 않다.
* 분할 과정에서 N-1 요소의 영역을 생성하는 경우(피벗이 최소값 똔느 최대값일 때), 최악의 경우 시간복잡도는 O(n*n)
* 최선의 경우는 두 개의 n/2 크기 리스트를 생성하게 되고, 이 최선의 경우와 평균 시간복잡도는 O(n log n)
* 퀵 정렬 알고리즘은 안정적이지 않음
"""


def quick_sort_cache(seq):
    """
    한 함수로 구현한다. (캐시 사용)
    :param seq:
    :return:
    """


if __name__ == "__main__":
    doctest.testmod()