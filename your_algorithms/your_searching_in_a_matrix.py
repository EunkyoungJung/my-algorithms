"""
다음 예제의 행렬은 한 행의 마지막 숫자가
다음 행의 첫번째 숫자보다 작다.
즉, 모든 행이 오름차순 정렬되어 있다.
이 행렬에서 어떤 숫자를 무차별(브루트포스)로 검색한다면,
시간복잡도는 O(mn)이다.
하지만 이 행렬은 모든 행이 정렬되어 있기 때문에 1차원 배열로 볼 수도 있다.
즉, O(log mn)의 이진 검색 알고리즘을 사용할 수 있다.
"""


def search_in_a_matrix(m1, value):
    rows = len(m1)
    columns = len(m1[0])

    lo = 0
    hi = rows*columns

    while lo < hi:
        mid = (lo + hi) // 2
        row = mid // columns
        column = mid % columns
        v = m1[row][column]
        if v == value:
            return True
        elif v > value:
            hi = mid
        else:
            lo = mid + 1
    return False


def test_search_in_a_matrix():
    a = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    import numpy
    b = numpy.array([(1, 2), (3, 4)])
    assert(search_in_a_matrix(a, 13) is True)
    assert(search_in_a_matrix(a, 14) is False)
    assert(search_in_a_matrix(b, 3) is True)
    assert(search_in_a_matrix(b, 5) is False)
    print("테스트 통과!")


if __name__ == "__main__":
    test_search_in_a_matrix()
