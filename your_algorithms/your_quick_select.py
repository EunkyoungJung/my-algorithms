import random


def quick_select_cache(seq, k):
    len_seq = len(seq)
    if len_seq < 2:
        return seq[0]

    # 피벗을 무작위로 선택할 수 있다
    # pivot = random.choice(seq)
    ipivot = len_seq // 2
    pivot = seq[ipivot]

    # seq의 값들 중에서 인덱스가 ipivot이 아니면서 seq[ipivot]보다 작거나 같은 친구들은 smallerList로!
    smallerList = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    largerList = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]


    # k번째로 작은 녀석을 찾는 로직!
    # k번째로 작은 녀석을 발견할 때까지 리스트를 반으로 나눈다(중간 원소보다 작은 것/큰것)
    m = len(smallerList)
    if k == m:
        return pivot
    elif k < m:
        return quick_select_cache(smallerList, k)
    else:
        return quick_select_cache(largerList, k-m-1)


def swap(seq, x, y):
    # x번 index의 값과 y번 index의 값을 서로 교체
    seq[x], seq[y] = seq[y], seq[x]


def quick_select(seq, k, left=None, right=None):
    # left와 right는 각각 int형인가보다
    left = left or 0
    right = right or len(seq) - 1
    ipivot = random.randint(left, right)
    pivot = seq[ipivot]

    # 피벗을 정렬 범위 밖으로 이동한다??
    swap(seq, ipivot, right)
    swapIndex, i = left, left

    # 왼쪽부터 오른쪽으로 차근차근히 비교해 나간다
    # pivot보다 작은 녀석들은 왼쪽으로 밀어넣는다
    while i < right:
        if pivot < seq[i]:
            swap(seq, i, swapIndex)
            swapIndex += 1 # swapIndex는 pivot보다느 큰 아이들이 나올때마다 1씩 증가한다
        i += 1

    # 피벗 위치를 확정한다??
    swap(seq, right, swapIndex)

    # 피벗 위치를 확인한다
    # rank는 전체에서 pivot보다 작은 아이들의 수!!!
    rank = len(seq) - swapIndex
    if k == rank:
        return seq[swapIndex]
    elif k < rank:
        return quick_select(seq, k, swapIndex+1, right)
    else:
        # k가 더 큰 경우
        return quick_select(seq, k, left, swapIndex-1)


if __name__ == "__main__":
    seq = [3, 7, 2, 1, 4, 6, 5, 10, 9, 11]
    k = len(seq) // 2
    print(sorted(seq))
    print(quick_select_cache(seq, k-1))

    # 아래 함수는 원본을 수정하므로 깊은 복사 실행
    import copy
    seq_copy = copy.deepcopy(seq)
    print(quick_select(seq_copy, k))

    # 중앙값(median) 출력을 위해서 넘파이를 사용함
    import numpy
    print(numpy.median(seq))

