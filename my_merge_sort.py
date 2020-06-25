"""
병합 정렬을 구현하는 여러가지 방법이 있다.
 => 시간 복잡도: 최악/최선/평균일 때 모두 O(n log n)
 => 공간 복잡도: 배열인 경우 O(n)이며, 일번적으로 제자리 정렬 (inplace)이 아니다.
 => 배열이 큰 경우 휴율적이다
 => 병합 정렬의 병합 함수를 사용하여, 두 배열을 병합한다.
 => 두 파일인 경우에도 병합이 가능하다.

 가) pop()메서드를 사용하여 다음과 같이 구현할 수 있다.
     (각 두 배열은 오름차순으로 정렬되어 있다.)
     def merge(left, right):
         if not left or not right: return left or right # 아무것도 병합하지 않는다.
         result = []
         while left and right:
             if left[-1] >= right[-1]:
                 result.append(left.pop())
             else:
                 result.append(right.pop())
         result.reverse()
         return (left or right) + result

        # >>>> l1 = [1, 2, 3, 4, 5, 6, 7]
        # >>>> l2 = [2, 4, 5, 8]
        # >>>> merge(l1, l2)
        [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]
"""


def my_merge_sort(seq):
    """
    1) pop()을 이용한 병합 정렬
    """
    print(f"input seq: {seq}")
    if len(seq) < 2: # 이건 무슨 경우?!
        return seq
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = my_merge_sort(left)
    if len(right) > 1:
        right = my_merge_sort(right)

    # left/right가 각각 1개씩이 되었을 때 밑에꺼를 실행
    res = []
    print(f"while 전: {left}, {right},// {res}")
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    print(f"while 후: {left}, {right},// {res}")
    res.reverse()
    return (left or right) + res


def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    print(f"최종 결과: {my_merge_sort(seq)}")



if __name__ == "__main__":
    test_merge_sort()