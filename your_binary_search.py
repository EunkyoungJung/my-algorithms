"""
이진 탐색 (Binary Search)
- 정렬된 배열 내에서 지정된 입력값의 위치(키)를 찾는다.
- 이진 검색은 알고리즘의 각 단계에서 입력값과 배열 중간 요소를 비교한다.
- 입력값과 중간 요소가 일치한다면, 배열의 위치가 반환된다.
- 입력값이 중간 요소보다 작으면, 중간 요소의 왼쪽 하위 배열에 검색 과정을 반복한다.
- 이진 검색의 시간복잡도는 O(log n)이다.
"""


def binary_search_rec(seq: list, target: int, low_index: int, high_index: int):
    """
    재귀함수 형태의 이진 탐색
    :param seq: 숫자로 이루어진 리스트
    :param target: 찾고자 하는 숫자 원소
    :param low_index: 최소 index 번호
    :param high_index: 최대 index 번호
    :return: seq에서 원소의 값이 target인 원소의 index 번호 리턴
    """
    if low_index > high_index:
        return None

    mid_index = (low_index + high_index) // 2
    if target == seq[mid_index]:
        return mid_index
    elif target < seq[mid_index]:
        return binary_search_rec(seq, target, low_index, mid_index - 1)
    else:
        return binary_search_rec(seq, target, mid_index + 1, high_index)


def binary_search_iter(seq: list, target: int):
    """
    반복문 형태의 이진 탐색
    :param seq: int로 이루어진 리스트
    :param target: int 원소
    :return:
    """
    high_index, low_index = len(seq), 0
    while low_index < high_index:
        mid_index = (high_index + low_index) // 2
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
    assert(binary_search_iter(seq, target) == 3)
    assert(binary_search_rec(seq, target, 0, len(seq)) == 3)
    print("테스트 통과!")


if __name__ == "__main__":
    test_binary_search()

