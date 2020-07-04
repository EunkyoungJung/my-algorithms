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
        smaller_than_pivot = [x for i,x in enumerate(seq) if x <= pivot_value and i != pivot_index]
        bigger_than_pivot = [x for i,x in enumerate(seq) if x > pivot_value and i != pivot_index]

        return quick_sort_cache(smaller_than_pivot) + [pivot_value] + quick_sort_cache(bigger_than_pivot)


########## 퀵 정렬 구현#2: 퀵 정렬을 두 함수로 나누어 구현 (캐시 사용)
def partition_devided(seq):
    pivot, seq = seq[0], seq[1:]
    before = []
    after = []
    before = [x for x in seq if x <= pivot]
    after = [x for x in seq if x > pivot]
    return before, pivot, after


def quick_sort_chache_devided(seq):
    if len(seq) < 2:
        return seq
    before, pivot, after = partition_devided(seq)
    return quick_sort_chache_devided(before) + [pivot] + quick_sort_chache_devided(after)


########## 퀵 정렬 구현#3 두 함수로 나누어서 구현 (캐시 사용 안함)
def partition(seq, start, end):
    pivot = seq[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and seq[left] <= pivot:
            left += 1
        while left <= right and pivot < seq[right]:
            right -= 1
        if right < left:
            done = True
        else:
            seq[left], seq[right] = seq[right], seq[left]
    seq[start], seq[right] = seq[right], seq[start]
    # print(right, seq)
    return right


def quick_sort(seq, start, end):
    if start < end:
        pivot = partition(seq, start, end)
        quick_sort(seq, start, pivot - 1)
        quick_sort(seq, pivot +1, end)
    return seq


def test_quick_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    # assert(quick_sort_cache(seq) == sorted(seq))
    # print(f"quick_sort_cache: {quick_sort_cache(seq)} // sorted: {sorted(seq)}")
    #assert(quick_sort_chache_devided(seq) == sorted(seq))
    print(f"quick_sort_cache_devided: {quick_sort_chache_devided(seq)} // sorted: {sorted(seq)}")
    #assert(quick_sort(seq, 0, len(seq)-1) == sorted(seq))
    print("테스트 통과")


if __name__ == "__main__":
    test_quick_sort()




