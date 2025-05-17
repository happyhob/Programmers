'''
정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.

단, arr에 2가 없는 경우 [-1]을 return 합니다.'''


def solution(arr):
    index =[]
    for i,a in enumerate(arr):
        if a ==2:
            index.append(i)
    if len(index)>=2:
         return [arr[a] for a in range(index[0],index[-1]+1)]
                 
    elif len(index)==0:
        return [-1]
    elif len(index)==1:
        return [2]


'''
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]

'''

'''
def solution(arr):
    answer = []
    check=[]
    if 2 not in arr:
        return [-1]
    else:
        for i in range(0, len(arr)):
            if arr[i]==2:
                check.append(i)
    return arr[check[0]:check[-1]+1]
'''
