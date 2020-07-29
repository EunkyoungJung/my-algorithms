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

    for i in range(2, number+1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[-1]


number = int(input())
print(find_last_fib(number))