"""
1. 문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

2. 입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

3. 출력
첫째 줄에 N!을 출력한다.
"""


def calculate_factorial(number: int) -> int:
    """
    :param number: factiroal을 계산하고자 하는 숫자
    :return: number! 결과

    >>> calculate_factorial(5)
    120
    >>> calculate_factorial(10)
    3628800
    >>> calculate_factorial(0)
    0
    >>> calculate_factorial(1)
    1
    """
    if number < 2:
        return number
    else:
        return number * calculate_factorial(number - 1)


def test_multiply_factorial():
    assert(calculate_factorial(5) == (1 * 2 * 3 * 4 * 5))
    assert (calculate_factorial(10) == (1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10))
    print("테스트 통과!")


if __name__ == "__main__":
    import doctest
    doctest.testmode()
    test_multiply_factorial()
