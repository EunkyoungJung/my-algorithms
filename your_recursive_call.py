"""
재귀 호출 (recursive call)
- 함수 안에서 동일한 함수를 호출하는 형태
- 여러 알고리즘 작성시 사용되므로, 익숙해져야 함
- 팩토리얼을 구하는 알고리즘을 recursive call을 활용해서 알고리즘 작성하기
- 재귀 함수는 내부적으로 스택처럼 관리된다
- 주의! 파이썬 재귀 함수는 한번에 호출되는 깊이가 1000회 이하여야함!
"""


# 여기서 질문!
# factorial을 돌리면 결론적으로 숫자가 나오는데
# 과정에서는 함수를 반환하기?도 함!
# 그러면 annotation의 return은 뭘로해줘야하는고얌?
def factorial_ver1(n: int):
    if n < 2: # n이 1인 경우 리턴
        # print(f"{n}")
        return 1 # 일정 값(1) 리턴하고 재귀 호출 종료
    # print(f"{n}*", end=" * ")
    return n * factorial_ver1(n-1) # 결과값을 리턴


def factorial_ver2(n: int):
    if n > 1: # n이 1인 경우 리턴
        # print(f"{n}", end=" * ")
        return n * factorial_ver2(n-1)
    # print(f"{n}")
    return 1 # 일정 값(1)을 리턴


def factorial_ver3(n: int):
    if n < 2: # n이 1인 경우 리턴
        # print(f"{n}")
        return 1 # 일정 값(1) 리턴하고 재귀 호출 종료
    # print(f"{n}", end=" * ")
    return_value = n * factorial_ver3(n-1)
    return return_value


def factorial_ver4(n: int):
    if n <= 1: # n이 1인 경우 리턴
        # print(f"{n}")
        return n # 재귀 호출 종료
    # print(f"{n}", end=" * ")
    return_value = n * factorial_ver4(n-1)
    return return_value


def test_factorials():
    assert(factorial_ver1(5) == 120)
    assert(factorial_ver2(5) == 120)
    assert(factorial_ver3(5) == 120)
    assert(factorial_ver4(5) == 120)
    print("테스트 통과!")


if __name__ == "__main__":
    test_factorials()