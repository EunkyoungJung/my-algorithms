from your_binary_search import binary_search_iter


def find_time_occurrence_list(seq, k):
    index_some_k = binary_search_iter(seq, k)
    count = 1
    sizet = len(seq)
    for i in range(index_some_k+1, sizet):
        if seq[i] == k:
            count += 1
        else:
            break
    for i in range(index_some_k-1, -1, -1):
        if seq[i] == k:
            count += 1
        else:
            break
    return count


def test_find_time_occurrence_list():
    seq = [1, 2, 2, 2 ,2, 2, 2, 5, 6, 6, 7, 8, 9]
    k = 2
    assert(find_time_occurrence_list(seq, k) == 6)
    print("테스트 통과!")


if __name__ == "__main__":
    test_find_time_occurrence_list()