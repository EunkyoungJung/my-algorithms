"""
행렬 검색:
- 각 행과 열이 정렬되어 있는 행렬에서 한 항목을 검색한다고 해보자.
- 즉, 모든 행은 왼쪽에서 오른쪽으로,
- 모든 열은 위에서 아래로 정렬(오름차순으로)되어 있다.
- 아래의 코드의 시간복잡도는 선형으로 O(m+n)이다.
"""


def is_in_matrix(matrix: list, value: int) -> bool:
    """
    입력된 matrix에서 입력된 value가 있는지 bool로 리턴하는 함수

    :param matrix: 숫자 원소로 이루어진 list의 list
    :param value: matrix에 존재한지 궁금한 int 원소
    :return: value가 matrix에 존재하면 True 리턴
    """
    found = False

    # 첫번째줄의 "맨끝 원소"부터 체크를 한다.
    row = 0
    column = len(matrix[0]) - 1

    while row < len(matrix) and column >= 0:
        if matrix[row][column] == value:
            found = True
            return found
        elif matrix[row][column] > value:
            column -= 1
        else:
            row += 1
    return found


def test_is_in_matrix():
    matrix1 = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    assert(is_in_matrix(matrix1, 8) is True)
    assert(is_in_matrix(matrix1, 3) is False)

    matrix2 = [[0]]
    assert(is_in_matrix(matrix2, 0) is True)

    print("테스트 통과")


if __name__ == "__main__":
    test_is_in_matrix()


