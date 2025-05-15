'''
문자열 my_string과 정수 배열 indices가 주어질 때, my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
'''

def solution(my_string, indices):
    result =''
    for i,s in enumerate(my_string):
        if i in indices:
            continue
        else:
            result+=s
    return result

'''
def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse=True):
        del my_string[i]
    return ''.join(my_string)
'''

'''
def solution(my_string, indices):
    return "".join([v for i,v in enumerate(my_string) if i not in indices])
'''

'''
def solution(my_string, indices):
    for idx in indices:
        my_string = my_string[:idx] + 'X' + my_string[idx+1:]
    return my_string.replace('X', '')
'''
