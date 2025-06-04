'''
정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.
'''

def solution(l, r):
    temp = []
    
    # 자릿수 구하기
    lenth = len(str(r))
    if r/(10**lenth)<5:
        lenth = lenth-1
    for i in range(0,lenth+1):
        tmp=[]
        current_len = 10**i # 1, 10, 100, 1000
        start = current_len *5 # 5, 50, 500, 5000 .....
        
        for n in temp:
            tmp.append(start+n)
        temp.append(start)
        temp = temp+tmp
        
    result = [t for t in temp if t>=l and t<=r]
    return  [-1] if result ==[] else result

'''
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]
'''

'''
def solution(l, r):
    answer = []
    i = 1
    n = 5

    while True:
        if n > r: break
        n = 5 * int(bin(i)[2:])
        if l <= n <= r:
            answer.append(n)
        i += 1

    return [-1] if len(answer) == 0 else answer

'''
