"""
리스트가 정렬되어 있다면,
리스트 안에 검색하려는 항목이 없는 경우에도
검색하려는 항목이 있을 때와 같은 실행 시간을 가질 수 있음
"""


def ordered_sequential_search(seq, n):
    item = 0
    for item in seq:
        if item > n: # 오름차순으로 가정하였음으로
            return False
        if item == n:
            return True
    return False


def test_ordered_sequential_search():
    seq = [1, 2, 4, 5, 6, 8, 10]
    n1 = 10
    n2 = 7
    assert(ordered_sequential_search(seq, n1) is True)
    assert(ordered_sequential_search(seq, n2) is False)
    print("테스트 통과!")


if __name__ == "__main__":
    test_ordered_sequential_search()