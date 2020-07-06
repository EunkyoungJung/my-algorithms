import random


def swap(seq, a, b):
    seq[a], seq[b] = seq[b], seq[a]


def find_kth_largest_number(seq, k, start_index=None, end_index=None):
    start_index = start_index or 0
    end_index = end_index or (len(seq) - 1)
    pivot_index = random.randint(start_index, end_index)
    pivot_value = seq[pivot_index]

    swap(seq, pivot_index, end_index)
    swap_index, i = start_index, start_index
    while i < end_index:
        if seq[i] < pivot_value:
            swap(seq, i, swap_index)
            swap_index += 1
        i += 1

    swap(seq, end_index, swap_index)

    rank = len(seq) - swap_index
    if k == rank:
        return seq[swap_index]
    elif k < rank:
        return find_kth_largest_number(seq, k, start_index=swap_index + 1, end_index=end_index)
    else:
        return find_kth_largest_number(seq, k, start_index=start_index, end_index=swap_index - 1)


def find_k_largest_numbers(seq, k):
    kth_largest_number = find_kth_largest_number(seq, k)

    result = []
    for item in seq:
        if item >= kth_largest_number:
            result.append(item)
    return result


if __name__ == "__main__":
    seq = [3, 10, 4, 5, 1, 8, 9, 11, 5]
    k = 3
    print(find_k_largest_numbers(seq, k))