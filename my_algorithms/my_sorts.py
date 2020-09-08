import doctest


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
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res


if __name__ == "__main__":
    doctest.testmod()