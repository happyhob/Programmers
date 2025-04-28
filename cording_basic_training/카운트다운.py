'''
정수 start_num와 end_num가 주어질 때, 
start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 

eturn하도록 solution 함수를 완성해주세요.
'''

def solution(start_num, end_num):
    arr=[]
    for i in range(0,start_num-end_num+1):
        arr.append(start_num-i)
        
    return arr

'''
def solution(start, end):
    return list(range(start,end-1,-1))

'''

'''
def solution(start, end):
    return [i for i in range(start,end-1,-1)]
'''

