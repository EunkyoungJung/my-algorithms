from my_algorithms.my_binary_search import iterative_binary_search


def count_ordered_list(seq, key) -> int:
    """
    key가 seq에서 몇 번 나오는지 횟수를 리턴
    :param seq: int로 이루어진 오름차순으로 정렬된 list
    :param key: seq에서 카운하고 싶은 int로 된 값
    :return: seq에서 key가 등장한 회수를 리턴
    """
    key_high_index = iterative_binary_search(seq, key)
    if key_high_index is None:
        return None
    count = 1
    seq_size = len(seq)

    for _ in range(key_high_index+1, seq_size):
        if seq[_] == key:
            count += 1
        else:
            break

    for _ in range(key_high_index-1, -1, -1):
        if seq[_] == key:
            count += 1
        else:
            break

    return count


def test_count():
    seq = [1, 2, 2, 2, 2, 2, 2, 5, 6, 6, 7, 8, 9]
    k = 2
    assert(count_ordered_list(seq, k) == 6)
    print("테스트 통과!")


if __name__ == "__main__":
    test_count()


