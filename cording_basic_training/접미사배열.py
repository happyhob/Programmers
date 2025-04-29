'''
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 
예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string이 매개변수로 주어질 때, 
my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
'''

def solution(my_string):
    return sorted([my_string[i:] for i in range(len(my_string))])


'''
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[-i:])
    answer.sort()
    return answer
'''



''' sorted 직접 구현해보기'''
### 병합정렬
def my_sorted(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = my_sorted(arr[:mid])
    right = my_sorted(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # 왼쪽과 오른쪽 배열을 비교하며 작은 값부터 넣는다
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 오름차순
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 요소들 추가
    result.extend(left[i:])
    result.extend(right[j:])
    return result


### 버블 정렬
def my_sorted(iterable, reverse=False):
    result = list(iterable)  # 원본을 복사
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            if (result[j] > result[j + 1]) != reverse:
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result
