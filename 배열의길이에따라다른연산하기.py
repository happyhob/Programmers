'''
길이가 홀수라면 > 모든 짝수 인덱스 위치에 n을 더함
짝수라면 > 모든 홀수 인덱스 위치에 n을 더한 배열을 return
'''


def solution(arr, n):
    arr_len = len(arr)
    if arr_len %2 ==0:
        answer =[ a+n if idx%2!=0 else a for idx,a in enumerate(arr) ]
    else:
         answer =[ a+n if idx%2==0 else a for idx,a in enumerate(arr) ]
    return answer