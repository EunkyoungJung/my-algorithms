"""
모든 행이 오름차순 정렬되어 있는 경우, matrix search
- 모든 행의 마지막 원소는 다음 행의 첫번째 숫자보다 작다.
- 이 행렬에서 어떤 숫자를 무차별(부르트 포스)로 검색한다면, 시간복잡도는 O(mn)이다.
- 하지만 이 행렬은 모든 행이 정렬되어 있기 때문에 1차원 배열로 볼 수도 있다.
- 즉, O(log mn)의 이진 검색 알고리즘을 사용할 수 있다.
"""


def is_in_sorted_matrix(sorted_matrix, target):
    rows = len(sorted_matrix)
    columns = len(sorted_matrix[0])

    # 행렬은 일차원 리스트로 간주하고 search
    # 왜냐하면 모든 행렬의 row들이 오름차순으로 정렬되어 있기 때문
    # row1 < row2 < row3

    # binary search로 target 찾기
    left_index = 0
    right_index = rows * columns
    while left_index < right_index:
        mid_index = (left_index + right_index) // 2
        # mid에 매칭되는 row/column 계산하기
        row = mid_index // columns
        column = mid_index % columns
        value = sorted_matrix[row][column]
        if target == value:
            return True
        elif target < value:
            right_index = mid_index
        else:
            left_index = mid_index + 1
    return False


def test_is_in_sorted_matrix():
    a = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    import numpy
    b = numpy.array([(1, 2), (3, 4)])
    assert(is_in_sorted_matrix(a, 13) is True)
    assert(is_in_sorted_matrix(a, 14) is False)
    assert(is_in_sorted_matrix(b, 3) is True)
    assert(is_in_sorted_matrix(b, 5) is False)
    print("테스트 통과!")


if __name__ == "__main__":
    test_is_in_sorted_matrix()

