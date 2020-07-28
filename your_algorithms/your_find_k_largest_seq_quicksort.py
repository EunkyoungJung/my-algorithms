import random


def swap(seq, x, y):
    seq[x], seq[y] = seq[y], seq[x]


def quick_select(seq, k, start=None, end=None):
    start = start or 0 # start가 없을 경우 0
    end = end or len(seq) - 1 # end가 없을 경우 seq의 마지막 원소의 인덱스
    pivot_index = random.randint(start, end) # start부터 end 바로 전까지의 임의의 정수
    pivot_value = seq[pivot_index] # 임의로 선정된 pivot_index의 value

    # 피벗을 정렬 범위 밖으로 이동한다
    swap(seq, pivot_index, end)  # seq[pivot_value]와 seq[end]를 swap
    swapIndex, i = start, start
    while i < end: # 처음부터 끝까지 비교
        if seq[i] < pivot_value: # pivot_value를 기준으로 작은 것들은
            swap(seq, i, swapIndex) # seq[i]와 seq[swapIndex]를 ?!
            swapIndex += 1
        i += 1

    # 피벗 위치를 확정한다
    # 선택된 피벗보다 마지막으로 작은 원소의 index!
    swap(seq, end, swapIndex)

    # 피벗 위치를 확인한다
    rank = len(seq) - swapIndex
    if k == rank:
        return seq[swapIndex]
    elif k < rank:
        return quick_select(seq, k, start=swapIndex + 1, end=end)
    else:
        return quick_select(seq, k, start=start, end=swapIndex - 1)


def find_k_largest_seq_quickselect(seq, k):
    # k번째로 큰 값을 찾는다.
    kth_largest = quick_select(seq, k)

    # k번째보다 큰 값을 저장한다.
    result = []
    for item in seq:
        if item >= kth_largest:
            result.append(item)
    return result


if __name__ == "__main__":
    seq = [3, 10, 4, 5, 1, 8, 9, 11, 5]
    k = 3
    print(find_k_largest_seq_quickselect(seq, k))