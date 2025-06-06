'''
정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.

arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.
'''


def solution(n):
    result =[]
    for i in range(0,n):
        tmp =[]
        for j in range(0,n):
            if i==j:
                tmp.append(1)
            else:
                tmp.append(0)
        result.append(tmp)
    return result

'''
def solution(n):
    answer=[[0]*n for i in range(n)]
    for i in range(n): answer[i][i]=1
    return answer
'''

'''
import numpy as np

def solution(n):
    return np.eye(n).tolist()

'''
# 파이썬 정적 배열 선언 및 초기화
cols =2
row = 3
arr = [[0 for _ in range(cols)] for _ in range(row)]
