"""
- 파이썬 같은 고급 언어는 반환 값을 "캐싱"하여 "재귀식"을 구현할 수 있음
- 같은 인수가 두 번 이상 호출되고, 그 결과가 캐시에 직접 반환되는 메모이제이션 메서드를 구현
"""


from functools import wraps
from your_benchmark import benchmark


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


@memo
def fib2(n):
    if n < 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


def fib3(m, n):
    if m[n] == 0:
        m[n] = fib3(m, n-1) + fib3(m, n-2)
    return m[n]


@benchmark
def test_fib(n):
    print(f"fib(n): {fib(n)}")


@benchmark
def test_fib2(n):
    print(f"fib2(n): {fib2(n)}")


@benchmark
def test_fib3(n):
    m = [0] * (n+1)
    m[0], m[1] = 1, 1
    print(f"fib3(m, n): {fib3(m, n)}")


if __name__ == "__main__":
    n = 35
    test_fib(n)
    test_fib2(n)
    test_fib3(n)
