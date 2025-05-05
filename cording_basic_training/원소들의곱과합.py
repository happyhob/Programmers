'''
정수가 담긴 리스트 num_list가 주어질 때,
모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

제한사항
'''

def solution(num_list):
    num_list_sum =0
    num_list_mul = 1
    for num in num_list:
        num_list_sum +=num
        num_list_mul *=num
    return 1 if num_list_sum**2> num_list_mul else 0


'''
def solution(num_list):
    mul = 1 
    for n in num_list:
        mul *= n
    return int(mul < sum(num_list) ** 2)
'''

'''
import math
def solution(num_list):
    answer = 0
    if math.prod(num_list) < (sum(num_list)**2):
        answer = 1
    return answer
'''