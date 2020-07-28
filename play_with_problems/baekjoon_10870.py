"""
1. 문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n>=2)가 된다.
n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

2. 입력
첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.

3. 출력
첫째 줄에 n번째 피보나치 수를 출력한다.
"""


def find_last_fib(number: int) -> int:
    """
    :param number: 피보나치 수열의 원소 개수
    :return: 피보나치 수열의 마지막 원소 리턴

    >>> find_last_fib(10)
    55
    """

    fib_list = [0, 1]
    if number == 0:
        return 0
    if number == 1:
        return 1

    for i in range(2, number + 1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmode()
