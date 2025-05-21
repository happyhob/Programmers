'''
문자열 my_string과 정수 s, e가 매개변수로 주어질 때, my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.
'''

def solution(my_string, s, e):
    list_str = list(my_string)
    
    temp = list_str[:s] + list_str[s:e+1][::-1] + list_str[e+1:]
    return "".join(temp)
'''
def solution(my_string, s, e):
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]
'''

'''
def solution(my_string, s, e):
    substr = reversed(list(my_string[s:e+1]))
    return my_string[:s] + ''.join(substr) + my_string[e+1:]
'''
