"""
이진 탐색을 사용하여 제곱근 구하기
"""


def find_sqrt_with_bin_search(num: int, error=0.001) -> float:
    lower = num < 1 and num or 1
    upper = num < 1 and 1 or num
    mid = lower + (upper - lower) / 2.0
    square = mid * mid
    while abs(square - num) > error:
        if square < num:
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
    print(find_sqrt_with_bin_search(a))
    print(math.sqrt(b))
    print(find_sqrt_with_bin_search(b))