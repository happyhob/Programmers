'''
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.

위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
'''

def solution(arr, queries):
    for query in queries:
        for i in range(query[0],query[1]+1):
            arr[i] +=1
    return arr
'''
def solution(arr, queries):
    for l,r in queries:
        for i in range(l,r+1): arr[i]+=1
    return arr
'''

'''
def solution(arr, queries):
    for (s, e) in queries:
        arr = [a+1 if s <= i <= e else a for i, a in enumerate(arr)]
    return arr
'''
