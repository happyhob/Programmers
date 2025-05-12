'''
알파벳 소문자로 이루어진 문자열 myString이 주어집니다. 
알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.
'''


def solution(myString):
    result =''
    for s in myString:
        if ord(s)-ord('l')<=0:
            result+='l'
        else:
            result+=s
    return result


'''
def solution(myString):
    return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))
'''

'''
def solution(myString):
    answer = [x if x > 'l' else 'l' for x in myString]
    return ''.join(answer)
'''
