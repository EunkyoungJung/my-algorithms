"""
파이썬 내장 bisect 모듈로 이진 검색을 할 수도 있음
bisect는 주어진 리스트에서 target의 위치를 찾는다.
- 그런데 시작번호가 0이 아니라 1이다!
- 없으면 0을 반환한다.
"""

from bisect import bisect


def test_bisect():
    seq = [1, 2, 5, 6, 7, 10, 12, 12, 14, 15]
    target = 6
    print(f"bsect(seq, target): {bisect(seq, target)}")
    assert(bisect(seq, target) == 4)
    assert (bisect(seq, -1) == 0)
    print("테스트 통과!")


if __name__ == "__main__":
    test_bisect()
