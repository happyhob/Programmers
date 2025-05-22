'''정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.

각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.


'''

def solution(arr, queries):
    result =[]
    for s,e,k in queries:
        value = [arr[i] for i in range(s,e+1) if arr[i]>k]
        if value ==[]:
            result.append(-1)
        else:
            result.append(min(value))
    return result


'''
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer
'''

'''
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        l = [i for i in arr[s:e+1] if i > k]
        answer.append(-1 if len(l) == 0 else min(l))
    return answer
'''

'''
def solution(arr, queries):
    return list(map(lambda x: -1 if x==10**6 else x, [min(list(filter(lambda x: x > k, arr[s:e+1])) + [10**6]) for s, e, k in queries]))

'''
