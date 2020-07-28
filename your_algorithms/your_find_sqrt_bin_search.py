"""
제곱근 계산하기
: 이진 검색을 사용하여 제곱근을 구할 수도 있다.
"""


def find_sqrt_bin_search(n, error=0.001):
    # lower = (n<1 and n) or 1
    # 즉 "1보다 작은수면 n 그대로", 1이상이면 무조건 1
    # 1 초과 버림
    lower = n < 1 and n or 1

    # lower = (n<1 and 1) or n
    # 즉, "1보닥 작은수면 무조건 1", 1이상이면 n 그대로
    # 1 미만 버림
    upper = n < 1 and 1 or n

    # "mid*mid"가 "n"이 되는 mid를 찾아라!
    mid = lower + (upper - lower) / 2.0
    square = mid * mid
    while abs(square - n) > error:
        if square < n:
            lower = mid
        else:
            upper = mid
        mid = lower + (upper - lower) / 2.0
        square = mid * mid
    return mid


if __name__ == "__main__":
    a = 2
    b = 9
    import math
    print(math.sqrt(a))
    print(find_sqrt_bin_search(a))
    print(math.sqrt(b))
    print(find_sqrt_bin_search(b))
