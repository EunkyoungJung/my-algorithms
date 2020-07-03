"""
병합 정렬(merge sort)
* 재귀용법을 활용한 정렬 알고리즘
   1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
   2. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
   3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.
"""

import random
data_list = random.sample(range(100), 10)

# print(data_list)


def merge(left, right):
    merged_list = list()
    left_index, right_index = 0, 0

    # case01: left/right 둘다 있을 때
    while len(left) > left_index and len(right) > right_index:
        if left[left_index] > right[right_index]:
            merged_list.append(right[right_index])
            right_index += 1
        else:
            merged_list.append(left[left_index])
            left_index += 1

    # case02: right 데이터가 없을 때
    while len(left) > left_index:
        merged_list.append(left[left_index])
        left_index += 1

    # case03: left 데이터가 없을 때
    while len(right) > right_index:
        merged_list.append(right[right_index])
        right_index += 1

    return merged_list


def merge_split(data_list):
    if len(data_list) < 2:
        return data_list
    medium = len(data_list) //2
    left = merge_split(data_list[:medium])
    right = merge_split(data_list[medium:])
    return merge(left, right)




print(f"merge 실행결과: {merge_split(data_list)}")