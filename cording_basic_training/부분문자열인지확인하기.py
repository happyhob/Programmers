'''
부분 문자열이란 문자열에서 연속된 일부분에 해당하는 문자열을 의미합니다. 예를 들어, 문자열 "ana", "ban", "anana", "banana", "n"는 모두 문자열 "banana"의 부분 문자열이지만, "aaa", "bnana", "wxyz"는 모두 "banana"의 부분 문자열이 아닙니다.

문자열 my_string과 target이 매개변수로 주어질 때, target이 문자열 my_string의 부분 문자열이라면 1을, 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
'''


def solution(my_string, target):
    if target in my_string:
        return 1
    else :
        return 0
'''
def solution(my_string, target):
    return int(target in my_string)
'''

'''

def solution(my_string, target):
    answer = 0

    my_string2 = list(my_string)

    for i in range(len(my_string)):
        if my_string2[:len(target)] == list(target):
            return 1
        my_string2.pop(0)

    return answer
'''

'''
def solution(my_string, target):
    answer = 0
    for i in range(len(my_string)):
        if i+len(target)>len(my_string):
            break
        test=my_string[i:i+len(target)]
        if test==target:
            answer=1

    return answer
'''
