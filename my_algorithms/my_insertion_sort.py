"""
삽입 정렬 (insertion sort)
- 최선의 경우(완전 정렬이 되어 있는 경우), 시간복잡도는 O(n)
- 평균과 최악의 경우, O(n*n) 더 자세하게는 n*(n-1)/2
- 배열 맨 처음 정렬된 부분에, 정렬이 되지 않은 다음 항목을 반복적으로 삽입하는 방식
- 데이터 크기가 작고 리스트가 이미 정렬되어 있으면,
  병합 정렬이나 퀵 정렬 같은 고급 알고리즘보다 성능이 더 좋다
  (즉, 미리 정렬된 리스트에 새 항목을 추가할 때 좋다)
"""


def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq


def insertion_sort_rec(seq, i=None):
    if i is None:
        i = len(seq) - 1
    if i == 0:
        return i
    insertion_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq


def test_insertion_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert(insertion_sort(seq) == sorted(seq))
    assert(insertion_sort_rec(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_insertion_sort()

