"""
순차검색(sequential search)
- 배열이 정렬되어 있지 않거나, 연결 리스트와 같이 입력이 동적으로 할당되는 경우 흔히 사용

리스트 항목에 대한 순차검색의 시간복잡도:
  - 최선의 경우 O(1)
  - 평균 O(n/2)
  - 최악 O(n)
  - 리스트에 검색하려는 항목이 없다면, 최악/최선/평균 모두 O(n)
"""


def sequential_search(seq, n):
    for item in seq:
        if item == n:
            return True
    return False


def test_sequential_search():
    seq = [1, 5, 6, 8, 3]
    n1 = 5
    n2 = 7
    assert(sequential_search(seq, n1) is True)
    assert(sequential_search(seq, n2) is False)
    print("테스트 통과!")


if __name__ == "__main__":
    test_sequential_search()