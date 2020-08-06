"""
분할 정복 알고리즘과 이진 탐색
* divide : 리스트를 두 개의 서브 리스트로 나눈다.
* conquer:
    - "검색할 숫자(search) > 중간값"이면, 뒷 부분의 서브 리스트에서 검색할 숫자를 찾는다.
    - "검색할 숫자(search) < 중간값"이면, 앞 부분의 서브 리스트에서 검색할 숫자를 찾는다.
"""

import doctest
import random
import datetime

def my_binary_search_func(data_list: list, find_data: int) -> bool:
    """
    이진탐색으로 찾고자하는 데이터가 있는 지 없는지 알려주는 함수
    :param data_list: 오름차순으로 정렬된 숫자로 이루어진 리스트
    :param find_data: 찾고자 하는 숫자 원소
    :return: find_dat를 data_list에서 찾으면 true를 반환

    >>> my_binary_search_func([1,2,3,4], 1)
    True
    >>> my_binary_search_func([1], 1)
    True
    >>> my_binary_search_func([1,2,3,4], 5)
    False
    >>> my_binary_search_func([], 1)
    False
    """

    if len(data_list) == 1:
        if data_list[0] == find_data:
            return True
        else:
            return False

    if len(data_list) == 0:
        return False

    mid = len(data_list) // 2
    if data_list[mid] == find_data:
        return True
    elif data_list[mid] > find_data:
        return my_binary_search_func(data_list[:mid], find_data)
    else:
        return my_binary_search_func(data_list[mid+1:], find_data)


if __name__ == "__main__":
    doctest.testmod()
    data_list = random.sample(range(10000000), 100000)
    data_list.sort()
    # print(datetime.datetime.now())
    start_time = datetime.datetime.now()
    my_binary_search_func(data_list, 11)
    end_time = datetime.datetime.now()
    print(f"end_time -start_time = {end_time} - {start_time} = {end_time - start_time}")
    # print(datetime.datetime.now())
