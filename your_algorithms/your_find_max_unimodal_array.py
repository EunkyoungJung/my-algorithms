"""
단봉형 배열:
배열 요소들의 산포도를 그렸을 때 값이 증가했다가 다시 감소하는 곡선인 경우,
이 배열을 단봉형(unimodal)이라고 한다.
봉오리가 1개라서 단봉형! 🛤
아래는 단봉형 배열에서 이진 검색을 사용하여 최댓값을 찾아본다.
"""


def find_max_unimodal_array(A:list) -> int:
    """
    숫자로 이루어진 list에서 최대값을 리턴하는 함수

    :param A: 숫자로 이루어진 list
    :return: list에서 가장 큰 숫자 return
    """
    if len(A) <= 2:
        return None

    left = 0
    right = len(A) - 1
    while right > left + 1: #요기서 +1 왜 해주는 걸까?
        mid = (left + right) // 2
        if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
            # A[mid-1] < A[mid] > A[mid+1]
            # 단봉형의 꼭대기!
            return A[mid]
        elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
            # A[mid-1] < A[mid] < A[mid+1]
            # 올라가는 등산길!
            # 아직 꼭대기까지 안갔음! 계속 올라가쎄용!
            left = mid
        else:
            # 내려가는 등산길
            # 봉오리로 가려면 다시 후진!
            right = mid
    return None


def test_find_max_unimodal_array():
    seq = [1, 2, 5, 6, 7, 10, 12, 9, 8, 7, 6]
    assert(find_max_unimodal_array(seq) == max(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_find_max_unimodal_array()