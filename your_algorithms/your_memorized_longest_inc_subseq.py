"""
최장 증가 부분열(longest increasing subsequence)

- 증가하는 순서대로(오름차순으로) 숫자를 고른 부분열의 길이가 최대가 되게 하면 된다.
- 예를 들어,
   리스트 [94, 8, 78, 22, 38, 79, 93, 8, 84, 39]가 있다고 하면,
   가장 길게 증가하는 부분 리스트는 [8, 22, 38, 79, 93] 또는 [8, 22, 38, 79, 84]가 될 것이다.

https://stackoverflow.com/questions/6184869/what-is-the-difference-between-memoization-and-dynamic-programming
"""


from bisect import bisect
from itertools import combinations
from functools import wraps

from your_algorithms.your_benchmark import benchmark


def naive_longest_inc_subseq(seq):
    """ 1) 단순한 방법 """
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
            if list(sub) == sorted(sub):
                return len(sub)


def dp_longest_inc_subseq(seq):
    """ 2) 동적 계획법 """
    L = [1] * len(seq)
    res = []
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1 + L[pre])
    return max(L)


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


def memoized_longest_inc_subseq(seq):
    """ 3) 메모이제이션 """
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1 + L(pre))
        return res
    return max(L(i) for i in range(len(seq)))


def longest_inc_bisec(seq):
    """ 4) 이진 검색 """
    end = []
    for val in seq:
        idx = bisect(end, val)
        if idx == len(end):
            end.append(val)
        else:
            end[idx] = val
        # print(end)
    return len(end)


@benchmark
def test_naive_longest_inc_subseq():
    print(naive_longest_inc_subseq(s1))


@benchmark
def test_dp_longest_inc_subseq():
    print(dp_longest_inc_subseq(s1))


@benchmark
def test_memoized_longest_inc_subseq():
    print(memoized_longest_inc_subseq(s1))


@benchmark
def test_longest_inc_bisec():
    print(longest_inc_bisec(s1))


if __name__ == "__main__":
    # from random import randrange
    # s1 = [randrange(100) for i in range(20)]
    s1 = [94, 8, 78, 22, 38, 79, 93, 8, 84, 39]
    print(s1)
    test_naive_longest_inc_subseq()
    test_dp_longest_inc_subseq()
    test_memoized_longest_inc_subseq()
    test_longest_inc_bisec()