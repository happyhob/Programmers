'''
선택 정렬 핵심 개념!!

기본 아이디어!:
  1. 배열서 최솟값(또는 최댓값)을 선택해서
  2. 현재 위치와 교환 하는 반복 작업
  
시간 복잡도 O(n^2)
특징
- 정렬이 되어 있어도 모든 요소를 비교해야 함 (비효율적)
- 안정 정렬이 아님: 같은 값의 순서가 바뀔 수 있음
- 구현이 단순하고 직관적임

'''

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 가장 작은 원소의 인덱스를 찾음
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 현재 위치(i)와 가장 작은 원소의 위치(min_idx)를 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 예제
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print("정렬된 리스트:", sorted_numbers)
vv
