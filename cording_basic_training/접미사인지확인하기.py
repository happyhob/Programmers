'''
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 
예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string과 is_suffix가 주어질 때, 
is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

'''

def solution(my_string, is_suffix):
    return next((1 for i in range(0,len(my_string)) if my_string[i:] == is_suffix),0)



'''
def solution(m, s):
    if m[-len(s):]==s: return 1
    return 0
'''

'''
def solution(my_string, is_suffix):
    return int(my_string[-len(is_suffix):] == is_suffix)
'''