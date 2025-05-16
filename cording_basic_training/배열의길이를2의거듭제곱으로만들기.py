'''
정수 배열 arr이 매개변수로 주어집니다.
arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다.
arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.
'''


def solution(arr):
    val =2
    while(1):
        if len(arr)==1:
            return arr
        elif len(arr)>val:
            val *=2
            continue
        elif len(arr)<val:
            arr.extend([0]*(val-len(arr)))
            return arr
        else:
            return arr

'''
def solution(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)
'''

'''
def solution(arr):
    answer = [2**i for i in range(11)]
    while len(arr) not in answer:
        arr.append(0)
    return arr
'''
