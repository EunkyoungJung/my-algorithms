"""
이진 탐색 (Binary Search)
- 정렬된 배열에서 입력값의 위치(키)를 찾는다.
- 각 단계에서 타겟값과 배열의 중간 요소를 비교한다.
- 타겟값과 배열의 중간 요소의 값이 동일하면 중간요소의 위치(인덱스)가 반환된다.
- 타겟밗이 배열의 중간 요소보다 작으면, 하위배열(seq[:mid])을 다시 이진 탐색한다.
- 타겞값이 배열의 중간 요소보다 크면, 상위배열(seq[mid:])을 다시 이진 탐색한다.
- 타겞값과 배열의 중간 요소와 같을 때 까지 반복한다.
- 이진 탐색의 시간복잡도는 O(log n)이다.
"""


def recursive_binary_search(seq: list, target: int, low_index: int, high_index: int):
    """
    재귀 함수 형태의 바이너리 서치
    :param seq: int 원소로 이루어진 오름차순으로 정렬된 리스트
    :param target: 리스트에서의 위치를 찾고자하는 원소의 값
    :param low_index: 최소 index
    :param high_index: 최대 index
    :return: list에서 target의 위치(index)를 리턴
    """

    if low_index > high_index:
        return None

    mid_index = (low_index + high_index) // 2
    if target == seq[mid_index]:
        return mid_index
    elif target < seq[mid_index]:
        return recursive_binary_search(seq, target, low_index, mid_index - 1)
    else:
        return recursive_binary_search(seq, target, mid_index + 1, high_index)


def iterative_binary_search(seq: list, target: int):
    """
    반복문 형태의 바이너리 서치
    :param seq: int 원소로 이루어진 오름차순으로 정렬된 리스트
    :param target: 리스트에서의 위치를 찾고자 하는 원소의 값
    :return: list에서 target의 마지막 위치(index)를 리턴
    """
    low_index, high_index = 0, len(seq)
    while low_index < high_index:
        mid_index = (low_index + high_index) // 2
        if target == seq[mid_index]:
            return mid_index
        elif target < seq[mid_index]:
            high_index = mid_index
        else:
            low_index = mid_index + 1
    return None


def test_binary_search():
    seq = [1, 2, 5, 6, 7, 10, 12, 12, 14, 15]
    target = 6
    assert(recursive_binary_search(seq, target, 0, len(seq)) == 3)
    assert(iterative_binary_search(seq, target) == 3)
    print("테스트 통과")


if __name__ == "__main__":
    test_binary_search()