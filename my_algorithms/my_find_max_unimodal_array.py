"""
단봉형(unimodal) 배열:
배열의 요소들의 산포도를 그렸을 때
값이 증가했다가 다시 감소한느 곡선(봉오리의 형태)이 경우,
그 배열을 단봉형(unimodal)이라고 한다.

봉오리가 1개라서 단봉형! 🛤
아래는 단봉형 배열에서 이진 검색을 사용하여 최댓값을 찾아보자!
"""


def find_max_in_unimodal_array(unimodal_array: list) -> int:
    """
    숫자로 이루어진 단봉형 배열에서 최대값을 리턴하는 함수

    :param unimodal_array: 단봉형의 int 리스트
    :return: 최대 int 리턴 (최대값이 없을 경우 리턴 None)
    """

    if len(unimodal_array) <= 2:
        # 산꼭대기가 있으려면 최소한 원소가 3개 이상이어야겠죠?
        return None

    # 이진탐색으로 최대값을 구해보자
    left = 0
    right = len(unimodal_array) - 1
    while right > left + 1:
        mid = (left + right) // 2
        if unimodal_array[mid-1] < unimodal_array[mid] and unimodal_array[mid+1] < unimodal_array[mid]:
            return unimodal_array[mid]
        elif unimodal_array[mid-1] < unimodal_array[mid] and unimodal_array[mid+1] > unimodal_array[mid]:
            left = mid
        else:
            right = mid
    return None


def test_find_max_in_unimodal_array():
    seq = [1, 2, 5, 6, 7, 10, 12, 9, 8, 7, 6]
    print(find_max_in_unimodal_array(seq))
    assert(find_max_in_unimodal_array(seq) == max(seq))
    print("테스트 통과!")


if __name__ =="__main__":
    test_find_max_in_unimodal_array()