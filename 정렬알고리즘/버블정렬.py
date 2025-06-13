'''
# 버블(거품) 정렬


✅ 개념 설명
인접한 두 원소를 비교해서 순서가 잘못된 경우 교환.

한 번의 반복이 끝나면 가장 큰 값이 맨 뒤로 "거품처럼" 올라간다.

시간 복잡도:

최악/평균: O(n²)

최선(이미 정렬된 경우): O(n)

🧠 동작 방식 예시
리스트 [5, 2, 4, 3, 1]이 있다면:

1회전: [2, 4, 3, 1, 5]

2회전: [2, 3, 1, 4, 5]

3회전: [2, 1, 3, 4, 5]

4회전: [1, 2, 3, 4, 5]



''''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # 최적화: 교환 없으면 종료
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # 인접 요소 비교
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 스왑
                swapped = True

        if not swapped:
            break  # 정렬 완료
    return arr
