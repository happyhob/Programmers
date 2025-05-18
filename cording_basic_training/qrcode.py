'''
두 정수 q, r과 문자열 code가 주어질 때, 
code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 
return 하는 solution 함수를 작성해 주세요.
'''

def solution(q, r, code):
    result =''
    for i,s in enumerate(code):
        if i%q ==r:
            result+=s
    return result

'''
def solution(q, r, code):
    return code[r::q]
'''

'''
def solution(q, r, code):
    return ''.join(code[i] for i in range(r, len(code), q))
'''
