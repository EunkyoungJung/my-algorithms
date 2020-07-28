"""
재귀 함수를 이용하여 1부터 num까지의 곱이 출력되는 함수
"""
import random


def recursive_multiply(num: int):
    if num > 1:
        return num * recursive_multiply(num-1)
    else:
        return 1


def sum_list(numbers: list):
    # return sum(numbers)
    result = 0
    for number in numbers:
        result += number
    return result


def recursive_sum_list(numbers: list):
    # print(numbers)
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + recursive_sum_list(numbers[1:])


def is_palindrome(line: str):
    reversed_line = line + " "
    reversed_line = reversed_line[:-1]
    # print(reversed_line)
    mid = len(reversed_line)//2
    for index in range(1, mid+1):
        if line[index] != reversed_line[index]:
            return False
    return True


def is_palindrome_with_recursive(line: str):
    # print(line)
    if len(line) <= 1:
        return True
    if line[0] == line[-1]: # 매회 첫번째와 마지막 만을 비교! 이렇게 단순화하는 것이 포인트!
        return is_palindrome_with_recursive(line[1:-1])
    else:
        return False


def recursive_even_odd_function(num: int):
    print(num, end=" ")
    if num == 1:
        return num
    if num % 2 == 0:
        return recursive_even_odd_function(num // 2)
    else:
        return recursive_even_odd_function(3 * num + 1)


def make_sum_with_one_two_three(num: int):
    if num < 0:
        return 0
    if num == 0:
        return 1
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4

    return make_sum_with_one_two_three(num - 1) + make_sum_with_one_two_three(num -2) + make_sum_with_one_two_three(num - 3)


def test():
    assert(recursive_multiply(5) == (1*2*3*4*5))
    # numbers = random.sample(range(100), 10)
    numbers = [1, 2, 3, 4, 5]
    assert(recursive_sum_list(numbers) == sum(numbers))
    # is_palindrome('motor ')
    assert(is_palindrome('motor') is True)
    assert(is_palindrome_with_recursive('motor') is False)
    assert(recursive_even_odd_function(3) == 1)
    print("테스트 통과!")


if __name__ == "__main__":
    test()
    make_sum_with_one_two_three(4)
