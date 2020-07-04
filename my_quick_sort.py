"""
퀵 정렬(Quick Sort)
- 피벗(pivot) 값을 잘 선택하는 것이 성능의 핵심
- 리스트에서 기준이 되는 하나의 요소를 고르는데 이를 '피벗'이라고 함
- 피벗 앞에는 피벗보다 작은 값이 오고, 피벗 뒤에는 피벗보다 큰 값이 오도록 피벗을 기준으로 리스트를 둘로 나눔
- 리스트의 중앙값(median)을 피벗으로 선택하는 것은 이미 정렬된 리스트에서 가장 적합한 선택이고,
- 정렬되지 않은 리스트 대부분에서도 다른 선택보다 나쁘지 않음

분할 과정에서 n-1 요소의 영역을 생성하는 경우(피벗이 최솟값 똔느 최댓값일 때),
최악의 경우 시간복잡도는 O(n2)이다.
최선의 경우는 두 개의 n/2 크기 리스트를 생성하게 되고,
이 최선의 경우와 평균 시간복잡도는 O(n log n)이다.
퀵 정렬 알고리즘은 안정적이지 않음
"""


########## 퀵 정렬 구현#1: 한 함수로 구현 (캐시 사용)
def quick_sort_cache(seq):
    if len(seq) < 2:
        return seq
    else:
        pivot_index = len(seq) // 2
        pivot_value = seq[pivot_index]
        smaller_than_pivot = [x for i, x in enumerate(seq) if x <= pivot_value and i != pivot_index]
        bigger_than_pivot = [x for i, x in enumerate(seq) if x > pivot_value and i != pivot_index]

        return quick_sort_cache(smaller_than_pivot) + [pivot_value] + quick_sort_cache(bigger_than_pivot)


########## 퀵 정렬 구현#2: 퀵 정렬을 두 함수로 나누어 구현 (캐시 사용)
def partition_devided(seq):
    # seq의 첫번째 원소를 무조건 피봇으로!
    # 비교 대상은 첫번째 원소를 제외한 나머지 원소를 대상!
    pivot_value, *new_seq = seq
    smaller_than_pivot, bigger_than_pivot = [], []
    smaller_than_pivot = [x for x in new_seq if x <= pivot_value]
    bigger_than_pivot = [x for x in new_seq if x > pivot_value]
    return smaller_than_pivot, pivot_value, bigger_than_pivot


def quick_sort_cache_devided(seq):
    if len(seq) < 2:
        return seq
    else:
        # # seq를 피봇기준으로 나눈는 로직은 partion_devided 함수가 알아서!
        smaller_than_pivot, pivot_value, bigger_than_pivot = partition_devided(seq)
        return quick_sort_cache_devided(smaller_than_pivot) + [pivot_value] + quick_sort_cache_devided(bigger_than_pivot)


########## 퀵 정렬 구현#3 두 함수로 나누어서 구현 (캐시 사용 안함)
def partition(seq, start, end):
    pivot_value = seq[start]
    left_index = start + 1 # 피봇보다 1 큰 index
    right_index = end # seq의 마지막 index
    done = False

    while not done:
        while left_index <= right_index and seq[left_index] <= pivot_value:
            # left index 계속 증가 pivot보다 작은 동안은!
            left_index += 1
        while left_index <= right_index and pivot_value < seq[right_index]:
            # right index 계속 감소 pivot보다 큰 경우에는!
            right_index -= 1
        if right_index < left_index: # left의 값이 계속커져서 right보다 커진 순간! 즉! 정렬완료!
            done = True
        else:
            # left보다 right의 index가 큰 경우
            # 결론적으로는 seq[left]가 seq[right]보다 커서 서로 바꿔줌
            # print(f"left_index: {left_index},{seq[left_index]} // right_index: {right_index},{seq[right_index]} // seq: {seq}")
            seq[left_index], seq[right_index] = seq[right_index], seq[left_index]

    # 정렬된 결과가 right는 pivot_index!
    seq[start], seq[right_index] = seq[right_index], seq[start]
    print(f"{seq} right_index: {right_index}, {start, seq[start]},  {right_index, seq[right_index]}")
    return right_index


def quick_sort_no_cache(seq, start, end):
    # seq를 계속 input으로 넣어 변경함으로써 cache가 필요없어용
    if start < end:
        pivot = partition(seq, start, end)
        quick_sort_no_cache(seq, start, pivot - 1) # pivot의 left를 리턴
        quick_sort_no_cache(seq, pivot + 1, end) # pivot의 right를 리턴
    return seq


def test_quick_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    # assert(quick_sort_cache(seq) == sorted(seq))
    # print(f"quick_sort_cache: {quick_sort_cache(seq)} // sorted: {sorted(seq)}")
    #assert(quick_sort_cache_devided(seq) == sorted(seq))
    # print(f"quick_sort_cache_devided: {quick_sort_cache_devided(seq)} // sorted: {sorted(seq)}")
    #assert(quick_sort(seq, 0, len(seq)-1) == sorted(seq))
    # print(f"quick_sort_no_cache: {quick_sort_no_cache(seq, 0, len(seq)-1)} // sorted: {sorted(seq)}")
    print("테스트 통과")


if __name__ == "__main__":
    test_quick_sort()




