'''
어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 
예를 들어, "banana"의 모든 접두사는
 "b", "ba", "ban", "bana", "banan", "banana"입니다.
문자열 my_string과 is_prefix가 주어질 때, 
is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.


'''

def solution(my_string, is_prefix):
    return next((1 for i in range(0,len(my_string)) if my_string[0:i] ==is_prefix),0)


'''
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))
'''


'''
def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)]==is_prefix:return 1
    return 0
'''

'''
def solution(my_string, is_prefix):
    return 1 if my_string.find(is_prefix) == 0 else 0
'''