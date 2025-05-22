'''
직사각형 형태의 그림 파일이 있고, 이 그림 파일은 1 × 1 크기의 정사각형 크기의 픽셀로 이루어져 있습니다. 
이 그림 파일을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질 때, 이 그림 파일을 가로 세로로 k배 늘린 그림 파일을 나타내도록 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

'''
#첫 번쨰 겁나 비효율적인 코
def solution(picture, k):
    answer =[]
    for p in picture:
        info = p[0]
        idx_list =[]
        p_list =list(p)
        for i,s in enumerate(p_list):
            if info ==s:
                continue
            else:
                idx_list.append(i)
                info=s
        tmp = []
        tmp.append("".join(p_list[:idx_list[0]])*k)

        for i in range(len(idx_list)-1):
            tmp.append("".join(p_list[idx_list[i]:idx_list[i+1]])*k)
            
        tmp.append("".join(p_list[idx_list[-1]:])*k)
        
        answer.append("".join(tmp))
        
    test=[]
    for a in answer:
        for i in range(k):
            test.append(a)
    return test

#두 번째 코드 리팩토링

def solution(picture, k):
    answer = []
    for row in picture:
        # 각 문자를 k번 반복해 가로 확대
        expanded_row = ''.join(char * k for char in row)
        # 가로 확대된 한 줄을 세로로 k번 반복
        for _ in range(k):
            answer.append(expanded_row)
    return answer


'''
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer
'''

'''
def solution(picture, k):

    answer = []

    for i in range(len(picture)):
        answer += [picture[i].replace('.', '.'*k).replace('x', 'x'*k)] * k

    return answer
'''
