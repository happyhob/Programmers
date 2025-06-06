'''
문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. 
queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. 
my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.
'''

def solution(my_string, queries):
    my_string = list(my_string)
    for a,b in queries:
        lenth =(b-a+1)//2
        for i in range(lenth):
            my_string[a+i], my_string[b-i] = my_string[b-i],my_string[a+i]
        
    return ''.join(my_string)


'''
def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)

'''

'''
def solution(my_string, queries):
    for (s, e) in queries:
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string

'''
