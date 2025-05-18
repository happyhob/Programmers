'''
알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, 
my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수, 
my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 
순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.
'''


def solution(my_string):
    result =[]
    for i in range(65,122+1-6):
        if i >90:
            i = i+6
        count =0
        for s in my_string:
            if ord(s) ==i:
                count +=1
        result.append(count)
    #65 ~ 90  # 대문자
    #97 ~ 122 # 소문자 
        
    return result

'''
def solution(my_string):
    answer=[0]*52
    for x in my_string:
        if x.isupper():
            answer[ord(x)-65]+=1
        else:
            answer[ord(x)-71]+=1
    return answer
'''
