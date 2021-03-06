"""
병합 정렬을 구현하는 여러가지 방법이 있다.
 => 시간 복잡도: 최악/최선/평균일 때 모두 O(n log n)
 => 공간 복잡도: 배열인 경우 O(n)이며, 일번적으로 제자리 정렬 (inplace)이 아니다.
 => 배열이 큰 경우 휴율적이다
 => 병합 정렬의 병합 함수를 사용하여, 두 배열을 병합한다.
 => 두 파일인 경우에도 병합이 가능하다.

 가) pop()메서드를 사용하여 다음과 같이 구현할 수 있다.
     (각 두 배열은 오름차순으로 정렬되어 있다.)
     def merge(left, right):
         if not left or not right: return left or right # 아무것도 병합하지 않는다.
         result = []
         while left and right:
             if left[-1] >= right[-1]:
                 result.append(left.pop())
             else:
                 result.append(right.pop())
         result.reverse()
         return (left or right) + result

        # >>>> l1 = [1, 2, 3, 4, 5, 6, 7]
        # >>>> l2 = [2, 4, 5, 8]
        # >>>> merge(l1, l2)
        [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]
"""


"""
1) pop()을 이용한 병합 정렬     
"""
def merge_sort(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    # res를 계속 초기화하고 있음!
    #     # 위의 결과로 얻은 left/right를 비교해서 정렬하는 용도임!
    res = []
    while left and right:
        # left/right는 오름차순으로 정렬되어 있는 상황임
        #         # 그러니, left/right의 마지막 원소는 left/right의 각 최대값임
        #         # left/right읭 각 마지막 원소를 비교해서 큰 아이들을 res에 append함
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse() # left/right 중에 큰거를 맨앞으로 되어 있어서 오름차순으로 하기위해 reverse!
    return (left or right) + res



"""
2) 두 함수로 나누어서 구현하는 방법
   - 한 함수에서는 배열을 나누고,
   - 또 다른 함수에는 배열을 병합한다  
"""
def merge_sort_sep(seq):
    # 원소가 1개일 경우!
    if len(seq) < 2:
        return seq
    else:
        mid = len(seq) // 2
        # 계속 반으로 쪼갠다!
        left = merge_sort_sep(seq[:mid])
        right = merge_sort_sep(seq[mid:])
        return merge(left, right)


def merge(left, right):
    # 반으로 쪼개고 쪼개서 처음에는 left/right에는 1개 이하의 원소들이 담기게되고
    # 1개 이하의 원소들이 오름차순으로 정렬된 result를 반환한다
    if not left or not right:
        return left or right
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    return result


# def test_merge_sort():
#     seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
#     print(f"input: {seq}")
#     # print(f"최종 결과: {merge_sort(seq)}")
#     print(f"최종 결과: {merge_sort_sep(seq)}")
#
#
# if __name__ == "__main__":
#     test_merge_sort()




"""
3) 각 두 배열은 정렬된 상태다.
시간복잡도는 O(2n)이다.
"""
def merge_2n(left, right):
    if not left or not right:
        return left or right
    result = []
    while left and right:
        if left[-1] >= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    result.reverse()
    return (left or right) + result

# def test_merge_sort():
#     l1 = [1, 2, 3, 4, 5, 6, 7]
#     l2 = [2, 4, 5, 8]
#     print(f"l1: {l1} // l2: {l2}")
#     print(f"최종 결과: {merge_2n(l1, l2)}")
#
#
# if __name__ == "__main__":
#     test_merge_sort()


"""
4) 제자리 정렬로 구현한다
   가정: 정렬할 각 2개읠 배열은 각각 정렬된 상태이다.
"""
# def merge_two_arrays_inplace(l1, l2):
#     if not l1 or not l2:
#         return l1 or l2
#     p2 = len(l2) - 1 # l2의 마지막 원소의 인덱스
#     p1 = len(l1) - len(l2) - 1 # 이것은 무엇을 위해 존재하는 변수일까? ['0'] 직전 인덱스
#     p12 = len(l1) - 1 # l1의 마지막 원소의 인덱스
#
#     # l2의 원소가 1개 이상일 때! 그리고 l1이 l2보다 길때! 진행!
#     print(f"이제 시작!!! p2: {p2} l2[p2]: {l2[p2]} / p1: {p1} l1[p1]: {l1[p1]} / p12: {p12} l1[p12]: {l1[p12]}")
#     while p2 >= 0 and p1 >= 0:
#         print(f">> 진행중! p2: {p2} l2[p2]: {l2[p2]} / p1: {p1} l1[p1]: {l1[p1]} / p12: {p12} l1[p12]: {l1[p12]} / p12: {p12} l1[p12]: {l1[p12]}")
#         item_to_be_merged = l2[p2] # l2의 마지막 원소
#         item_bigger_array = l1[p1] # l1에서 l2의 개수만큼의 ['0']을 제외한 마지막 원소
#         if item_to_be_merged < item_bigger_array:
#             l1[p12] = item_bigger_array
#             p1 -= 1
#         else:
#             l1[p12] = item_to_be_merged
#             p2 -= 1
#         p12 -= 1
#         print(f">>>> 진행중! p2: {p2} l2[p2]: {l2[p2]} / p1: {p1} l1[p1]: {l1[p1]} / p12: {p12} l1[p12]: {l1[p12]} // l1: {l1} // l2: {l2}")
#     return l1


def merge_two_arrays_inplace(l1, l2):
    if not l1 or not l2:
        return l1 or l2

    l1_current_item_index = len(l1) - len(l2) - 1
    l2_current_item_index = len(l2) - 1
    l1_current_merge_index = len(l1) - 1

    while l2_current_item_index >= 0 and l1_current_merge_index >= 0:
        item_to_be_merged = l2[l2_current_item_index]
        item_bigger_array = l1[l1_current_item_index]
        if item_to_be_merged < item_bigger_array:
            l1[l1_current_merge_index] = item_bigger_array
            l1_current_item_index -= 1
        else:
            l1[l1_current_merge_index] = item_to_be_merged
            l2_current_item_index -= 1
        l1_current_merge_index -= 1
    return l1


# def test_merge_sort():
#     l1 = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0]
#     l2 = [2, 4, 5, 8]
#     print(f"l1: {l1} // l2: {l2}")
#     print(f"최종 결과: {merge_two_arrays_inplace(l1, l2)}")
#
#
# if __name__ == "__main__":
#     test_merge_sort()


"""
5) 파일을 병합한다
"""
def merge_files(list_files):
    result = []
    final = []
    for filename in list_files:
        aux = []
        with open(filename, "r") as file:
            for line in file:
                aux.append(int(line))
        result.append(aux)
    final.extend(result.pop())
    for l in result:
        final = merge(l, final)
    return final


def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    seq_sorted = sorted(seq)
    # print(seq_sorted, merge_sort(seq))
    assert(merge_sort(seq) == seq_sorted)
    assert(merge_sort_sep(seq) == seq_sorted)

    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = [2, 4, 5, 8]
    l_sorted = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]
    assert(merge_2n(l1, l2) == l_sorted)

    l1 = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0]
    l2 = [2, 4, 5, 8]
    l_sorted = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]
    assert(merge_two_arrays_inplace(l1, l2) == l_sorted)
    list_files = ["a.dat", "b.dat", "c.dat"]
    l_sorted = [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
    assert(merge_files(list_files) == l_sorted)
    print("테스트 통과!")


if __name__ == "__main__":
    test_merge_sort()