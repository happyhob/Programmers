'''
🔹 퀵 정렬 (Quick Sort)
✅ 핵심 개념 분할 정복(divide and conquer) 전략을 사용.

pivot과 partitioning

하나의 피벗(pivot)을 기준으로 왼쪽에는 작은 값, 오른쪽에는 큰 값을 나누고, 각각 다시 정렬을 재귀적으로 수행.

평균 시간 복잡도: O(n log n)

최악의 경우(이미 정렬된 경우 등): O(n²)

unstable sorting
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # 첫 번째 요소를 피벗으로 선택
    left = [x for x in arr[1:] if x <= pivot]  # 피벗보다 작거나 같은 값
    right = [x for x in arr[1:] if x > pivot]  # 피벗보다 큰 값
    return quick_sort(left) + [pivot] + quick_sort(right)

# 예시
arr = [5, 3, 8, 4, 2, 7, 1, 10]
sorted_arr = quick_sort(arr)
print(sorted_arr)
