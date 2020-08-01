from my_binary_search import iterative_binary_search


# 파이썬 set 사용
def intersection_with_sets(seq1, seq2):
    set1 = set(seq1)
    set2 = set(seq2)
    return set1.intersection(set2)


# 병합 정렬 사용
def intersection_with_merge_sort(seq1, seq2):
    result = []
    while seq1 and seq2:
        if seq1[-1] == seq2[-1]:
            # 같을 때는 seq1 것만 result에 넣는다
            result.append(seq1.pop())
            seq2.pop()

        # 아래의 2 경우는 같지 않은 경우!
        elif seq1[-1] > seq2[-1]:
            seq1.pop()
        else:
            seq2.pop()
    result.reverse()
    return result


# 이진 검색 사용
def intersection_with_binary_search(seq1, seq2):
    if len(seq1) > len(seq2):
        seq, keys = seq1, seq2
    else:
        seq, keys = seq2, seq1
    intersection = []

    for item in keys:
        if iterative_binary_search(seq, item):
            intersection.append(item)
    return intersection


def test_intersection_two_arrays():
    seq1 = [1, 2, 3, 5, 7, 8]
    seq2 = [3, 5, 6]
    assert(set(intersection_with_sets(seq1, seq2)) == set([3, 5]))
    assert(intersection_with_merge_sort(seq1, seq2) == [3, 5])
    assert(intersection_with_binary_search(seq1, seq2) == [3, 5])
    print("테스트 통과!")


if __name__ == "__main__":
    test_intersection_two_arrays()

