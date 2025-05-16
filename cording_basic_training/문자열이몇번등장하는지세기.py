'''
문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.
'''


def solution(myString, pat):
    count =0
    for i in range(len(myString)):
        if pat in myString[i:i+len(pat)]:
            count+=1
            
    return count


'''
def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :
            answer += 1
    return answer
'''

'''
def solution(myString, pat):
    return sum(myString[i:i + len(pat)] == pat for i in range(len(myString)))
'''

'''
def solution(myString, pat):
    answer=0
    for i in range(len(myString)):
        if myString[i:i+len(pat)]==pat:answer+=1
    return answer
'''
