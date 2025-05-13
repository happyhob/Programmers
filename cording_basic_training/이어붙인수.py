'''
정수가 담긴 리스트 num_list가 주어집니다. 
num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
'''

def solution(num_list):
    value1 = ''.join([str(num) for num in num_list if num%2!=0])
    value2 = ''.join([str(num) for num in num_list if num%2==0])
    return int(value1)+int(value2)
