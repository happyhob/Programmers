def solution(arr):
    answer = []
    for a in arr:
        for i in range(0,a):
            answer.append(a)
    return answer



'''
def solution(arr):
    return [i for i in arr for j in range(i)]
'''