"""
동적 계획법(Dynamic Programming)
"""


def recursive_fib(num: int):
    if num <= 1:
        return num
    else:
        return recursive_fib(num - 1) + recursive_fib(num - 2)


def dynamic_fib(num: int):
    cache = [0 for index in range(num + 1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num+1):
        cache[index] = cache[index - 1] + cache[index - 2]
    return cache[-1]


def test():
    assert(recursive_fib(10) == 55)
    assert(dynamic_fib(10) == 55)


if __name__ == "__main__":
    test()
