'''
# 셸 정렬

✅ 개념 설명
삽입 정렬의 개선판.

먼 거리의 원소끼리 먼저 비교 및 교환하며 점차 간격을 좁혀감.

마지막에는 간격을 1로 해서 삽입 정렬과 유사하게 마무리.

시간 복잡도:

일반적으로 O(n^1.3 ~ n^1.5)

특정 gap 사용 시 최악: O(n²)

🔩 간격(gap) 예시
간격을 n//2, n//4, ..., 1 순으로 설정 (전통적인 방법)
'''

#기본 셸 정렬
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # 초기 간격

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # 삽입 정렬처럼 처리 (간격을 둔 비교)
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # 간격 축소
    return arr


arr = [7,6,8,9,3,2,10,5,1]
shell_sort(arr)
