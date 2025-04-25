'''
알파벳으로 이루어진 문자열 myString이 주어집니다.
 모든 알파벳을 소문자로 변환하여 return 하는 solution 함수를 완성해 주세요.
'''



def solution(myString):
    return myString.lower()
    


''' 
def solution(myString):
    answer = ""
    for i in myString:
        if ord(i) < 95:
            i = ord(i) + 32
            answer += str(chr(i))
        else:
            answer += i

    return answer

'''