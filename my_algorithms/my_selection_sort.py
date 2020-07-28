"""
선택정렬 (selection sort)
- 먼저 리스트에서 가장 작거나 큰 항목을 찾아서(선택) 첫 번째 항목과 위치를 바꾼다.
- 그러고 나서 그 다음 항목을 찾아서(선택) 두 번쩨 항목과 위치를 바꾼다
- 이런식으로 리스트 끝에 도달할 때까지 이 과정을 반복한다.
- 리스트가 이미 정렬되어 있어도 시간복잡도는 O(n*n) (안정적이지도 않다)
- n*(n-1)/2

<선택 정렬 알고리즘>
1. 주어진 데이터 중, 최소값을 찾음
2. 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함
"""


def selection_sort(seq):
    # 오름차순 정렬
    length = len(seq)
    for i in range(length-1):
        min_j = i
        for j in range(i+1, length):
            if seq[min_j] > seq[j]:
                min_j = j
        seq[i], seq[min_j] = seq[min_j], seq[i]
    return seq


def test_selection_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert(selection_sort(seq) == sorted(seq))
    print("테스트 통과")


if __name__ == "__main__":
    test_selection_sort()