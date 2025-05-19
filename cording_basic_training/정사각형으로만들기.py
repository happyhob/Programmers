'''
이차원 정수 배열 arr이 매개변수로 주어집니다. 
arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 
열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
'''

def solution(arr):
    len1D = len(arr)
    len2D = len(arr[0])
    
    if len1D< len2D:
        for i in range(len2D-len1D):
            tmp=[]
            for i in range(len2D):
                tmp.append(0)
            arr.append(tmp)

    elif len1D>len2D:
        for a in arr:
            if len(a)<len1D:
                for i in range(len1D-len(a)):
                    a.append(0)
    
    return arr

'''
def solution(arr):
    n=len(arr)
    m=len(arr[0])
    if n>m:
        for i in range(n):
            for j in range(n-m):
                arr[i].append(0)
    else:
        for i in range(m-n):
            arr.append([0]*m)

    return arr
'''

'''
def solution(arr):
    answer = []
    x = len(arr)
    y = len(arr[0])
    m = max(x, y)

    answer=[[0]*m for i in range(m)]

    for i in range(x):
        for j in range(y):
            answer[i][j] = arr[i][j]

    return answer
'''
