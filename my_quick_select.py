import random

"""
오름차순으로 정렬된 list에서 k번째 큰 원소를 찾는 로직입니다.
"""


def quick_select_cache(seq: list, k: int):
    """입력된 리스트에서 k번째로 큰 원소(int)를 반환하는 함수
    :param seq: 원소가 int인 리스트
    :param k: 오름차순으로 정렬된 리스트의 몇번째 원소를 가르키는지 나타내는 int
    :return:
    """

    len_seq = len(seq)

    # 원소가 1개 인 경우
    if len_seq < 2:
        return seq[0]

    # pivot 값을 무작위로 선택할 수도 있음
    # pivot = random.choice(seq)
    pivot_index = len_seq // 2
    pivot_value = seq[pivot_index]

    smaller_than_pivot = [x for idx, x in enumerate(seq) if idx != pivot_index and x <= pivot_value]
    bigger_than_pivot = [x for idx, x in enumerate(seq) if idx != pivot_index and x > pivot_value]

    # k번째로 작은 녀석을 찾는 로직
    m = len(smaller_than_pivot)
    if k == m:
        return pivot_value
    elif k < m:
        return quick_select_cache(smaller_than_pivot, k)
    else:
        return quick_select_cache(bigger_than_pivot, k-m-1)


def swap(seq: list, x: int, y: int) -> None:
    seq[x], seq[y] = seq[y], seq[x]


def quick_select(seq: list, k: int, left=None, right=None) -> int:
    """오름차순으로 정렬된 리스트에서 k번째 원소(int)를 리턴한다.
    :param seq: 오름차순으로 정렬된 int로 구성된 list
    :param k: 몇 번째 원소를 추출할 지
    :param left: 왼쪽 index
    :param right: 오른쪽 index
    :return:
    """
    left = left or 0
    right = right or len(seq)-1

    pivot_index = random.randint(left, right)
    pivot_value = seq[pivot_index]

    # 피벗값을 맨 오른쪽에다가 갔다 놓는다
    swap(seq, pivot_index, right)
    swap_index, i = left, left

    while i < right:
        if pivot_value < seq[i]:
            # pivot_value보다 작은 녀석들은 왼쪽으로 몰아준다
            swap(seq, i, swap_index)
            swap_index += 1 #swapIndex는 pivot_value보다 작은 아이들의 숫자임
        i += 1

    swap(seq, right, swap_index)

    rank = len(seq) - swap_index # 전체에서 pivot_value보다 큰 원소들의 수
    if k == rank:
        return seq[swap_index]
    elif k < rank:
        return quick_select(seq, k, swap_index+1, right)
    else:
        return quick_select(seq, k, left, swap_index-1)


if __name__ == "__main__":
    seq = [3, 7, 2, 1, 4, 6, 5, 10, 9, 11]
    k = len(seq) // 2
    print(sorted(seq))
    print(quick_select_cache(seq, k-1))

    import copy
    seq_copy = copy.deepcopy(seq)
    print(quick_select(seq_copy, k))

    import numpy
    print(numpy.median(seq))

