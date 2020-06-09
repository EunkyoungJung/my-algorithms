import heapq

def merge_sorted_seqs(seq1, seq2):
    result = list()
    # print(heapq.merge(seq1, seq2))
    # <generator object merge at 0x000002BE6FB02348>
    for c in heapq.merge(seq1, seq2):
        result.append(c)
    return result

def test_merge_sorted_seq():
    seq1 = [1, 2, 3, 8, 9, 10]
    seq2 = [2, 3, 4, 5, 6, 7, 9]
    seq3 = seq1 + seq2
    assert(merge_sorted_seqs(seq1, seq2) == sorted(seq3))

    print("테스트 통과!")

if __name__ == "__main__":
    test_merge_sorted_seq()
