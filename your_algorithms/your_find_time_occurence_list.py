from your_algorithms.your_binary_search import binary_search_iter


def find_time_occurrence_list(seq, k) -> int:
    """
    k가 seq에서 몇번 나오는 지 횟수를 리턴
    :param seq: 숫자로 이루어진 list
    :param k: seq에서 등장 횟수를 찾고하자는 숫자
    :return: seq에서 k가 등장한 횟수를 리턴
    """

    # seq에 k가 가장 마지막에 등장한 index를 리턴
    index_some_k = binary_search_iter(seq, k)

    count = 1
    sizet = len(seq)

    # 뒤로 k를 찾는다
    for i in range(index_some_k+1, sizet):
        if seq[i] == k:
            count += 1
        else:
            break
    # 앞으로 k를 찾는다
    for i in range(index_some_k-1, -1, -1):
        if seq[i] == k:
            count += 1
        else:
            break
    return count


def test_find_time_occurrence_list():
    seq = [1, 2, 2, 2, 2, 2, 2, 5, 6, 6, 7, 8, 9]
    k = 2
    assert(find_time_occurrence_list(seq, k) == 6)
    print("테스트 통과!")


if __name__ == "__main__":
    test_find_time_occurrence_list()