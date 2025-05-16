'''
문자열 myString과 pat가 주어집니다. myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.
'''

def solution(myString, pat):
    value = 0
    for i in range(len(myString)):
        if pat ==myString[i:i+len(pat)]:
            value = i
    return myString[:value+len(pat)]

'''
solution=lambda x,y:x[:x.rindex(y)+len(y)]
'''

'''
def solution(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]
'''

'''
def solution(myString, pat):
    return myString[0:myString.rfind(pat)] + pat
'''

'''
def solution(myString, pat):
    return myString[:myString.rfind(pat) + len(pat)]
'''
