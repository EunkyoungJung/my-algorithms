import string
import collections

from my_deque import Deque

STRIP = string.whitespace + string.punctuation + "\"'"


def palindrome_checker_with_deque(str1):
    d1 = Deque()
    d2 = collections.deque()

    for s in str1.lower():
        if s not in STRIP:
            d1.enqueue(s)
            d2.append(s)

    # my_deque 파일의 Deque를 이용해서 푸는 방법
    eq1 = True
    while d1.size() > 1 and eq1:
        if d1.dequeue_front() != d1.dequeue():
            eq1 = False

    # collections의 deque를 이용해서 푸는 방법
    eq2 = True
    while len(d2) > 1 and eq2:
        if d2.pop() != d2.popleft():
            eq2 = False

    return eq1, eq2


if __name__ == "__main__":
    str1 = "Madam Im Adam"
    str2 = "Buffy is a Slayer"
    print(palindrome_checker_with_deque(str1))
    print(palindrome_checker_with_deque(str2))

