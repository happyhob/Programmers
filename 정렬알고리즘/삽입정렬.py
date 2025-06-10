'''
삽입 정렬 핵심 개념!!

기본 아이디어:
  1. 앞에서부터 차례대로 데이터를 확인하면서
  2. 자기보다 앞에 있는 정렬된 부분과 비교하여
  3. 적절한 위치에 삽입하는 방식
특징:
- 거의 정렬된 상태에서 매우 빠름
- 안정 정렬: 같은 값의 순서를 유지함
- 구현이 쉽고, 작은 데이터에 효율적
'''

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # 현재 삽입할 값
        j = i - 1
        # key보다 큰 값을 오른쪽으로 한 칸씩 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # key를 올바른 위치에 삽입
        arr[j + 1] = key
    return arr

# 예제
numbers = [64, 25, 12, 22, 11]
sorted_numbers = insert_sort(numbers)
print("정렬된 리스트:", sorted_numbers)
ㅍㅍㅍㅍㅍㅍㅍ
