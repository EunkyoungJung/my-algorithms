"""
거품 정렬 (bubble sort)
- 인접한 두 항목을 비교하여 정렬하는 방식
- 시간복잡도는 O(n*n)
- 최악의 경우의 시간복잡도는 n*(n-1)/2
- 완전 정렬되어 있는 상태라면 최선은 O(n)
- 항목이 수면 위로 거품처럼 올라오는 듯한 모습을 보이기 때문에 붙은 이름
"""


def bubble_sort(seq):
    length = len(seq) - 1
    for num in range(length, 0, -1):
        swap = 0
        for i in range(num):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                swap += 1
        print(f"{num}: {seq}/swap: {swap}")
        if swap == 0:
            break
    return seq


def test_bubble_sort():
    seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    # print(bubble_sort(seq), sorted(seq))
    assert(bubble_sort(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_bubble_sort()