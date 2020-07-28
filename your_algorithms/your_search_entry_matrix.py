"""
행렬 검색
: 각 행과 열이 정렬되어 있는 행렬에서 한 항목을 검색한다고 해보자.
즉, 모든 행은 왼쪽에서 오른쪽으로,
모든 열은 위에서 아래로 정렬(오름차순)되어 있다.
다음 코드의 시간복잡도는 선형으로 O(m+n)이다.
"""


def find_element_matrix_bool(m1: list, value: int) -> bool:
    """
    입력된 행렬(오름차순으로 정렬됨-기준:행/열)에서 입력받은 value가 존재하는지 확인하는 함수
    :param m1: n*m의 행렬
    :param value: 행렬에서 찾고자 하는 int값
    :return: 입력된 m1(행렬)에서 value를 찾으면 True를 리턴
    """
    found = False
    row = 0
    col = len(m1[0]) - 1
    while row < len(m1) and col >= 0:
        if m1[row][col] == value:
            found = True
            break
        elif m1[row][col] > value:
            col -= 1
        else:
            row += 1
    return found


def test_find_elem_matrix_bool():
    m1 = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    assert(find_element_matrix_bool(m1, 8) is True)
    assert(find_element_matrix_bool(m1, 3) is False)
    m2 = [[0]]
    assert(find_element_matrix_bool(m2, 0) is True)
    print("테스트 통과!")


if __name__ == "__main__":
    test_find_elem_matrix_bool()
