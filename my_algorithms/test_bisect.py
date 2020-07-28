"""
파이썬 내장 bisect 모듈로 이진 검색을 할 수도 있음
bisect()는 오름차순으로 정렬된 시퀀스에 target값이 "들어갈 위치"를 리턴
target이 해당리스트에 존재할 경우: bisect, bisect_right, bisect_left가 모두다 동일
target이 해당리스트에 없을 경우: bisect, bisect_right는 동일! 하지만 bisect_left는 다름!
"""

from bisect import bisect, bisect_left, bisect_right


def test_bisect():
    seq = [1, 2, 5, 6, 7, 10, 12, 12, 14, 15]

    target = 8
    # seq에서 "8(target)"을 삽입한다면 "7(인덱스번호:4번)"다음의 위치인 index 5번에 들어간다.
    print(f"bisect({seq}, {target}): {bisect(seq, target)}")
    print(f"bisect_right({seq}, {target}): {bisect_right(seq, target)}")
    print(f"bisect_left({seq}, {target}): {bisect_left(seq, target)}")
    """
    bisect([1, 2, 5, 6, 7, 10, 12, 12, 14, 15], 8): 5
    bisect_right([1, 2, 5, 6, 7, 10, 12, 12, 14, 15], 8): 5
    bisect_left([1, 2, 5, 6, 7, 10, 12, 12, 14, 15], 8): 5
    """

    target = 7
    # seq에서 "7(target)"을 삽입한다면 "7(인덱스번호:4번)"다음의 위치인 index 5번에 들어간다.
    # 다만 "7"이 이미 seq에 존재한다.
    # 이럴 경우, bisect_left는 "7"의 위치인 인덱스 4를 리턴한다.
    print(f"bisect({seq}, {target}): {bisect(seq, target)}")
    print(f"bisect_right({seq}, {target}): {bisect_right(seq, target)}")
    print(f"bisect_left({seq}, {target}): {bisect_left(seq, target)}")
    """
    bisect([1, 2, 5, 6, 7, 10, 12, 12, 14, 15], 7): 5
    bisect_right([1, 2, 5, 6, 7, 10, 12, 12, 14, 15], 7): 5
    bisect_left([1, 2, 5, 6, 7, 10, 12, 12, 14, 15], 7): 4
    """

    target = -1
    # seq에서 "-1(target)"을 삽입한다면 -1 보다 작은 원소가 없음으로 첫번째(인덱스 0)에 삽입된다.
    print(f"bisect({seq}, {target}): {bisect(seq, target)}")
    print(f"bisect_right({seq}, {target}): {bisect_right(seq, target)}")
    print(f"bisect_left({seq}, {target}): {bisect_left(seq, target)}")
    """
    bisect([1, 2, 5, 6, 7, 10, 12, 12, 14, 15], -1): 0
    bisect_right([1, 2, 5, 6, 7, 10, 12, 12, 14, 15], -1): 0
    bisect_left([1, 2, 5, 6, 7, 10, 12, 12, 14, 15], -1): 0
    """


if __name__ == "__main__":
    test_bisect()
