'''
정수 리스트 num_list가 주어질 때, 
첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 
음수가 없다면 -1을 return합니다.
'''
def solution(num_list):
    # if [idx  for idx,num in enumerate(num_list) if num<0] ==[]:
    #     return -1
    # else:
    #      return [idx  for idx,num in enumerate(num_list) if num<0][0]
        
    return next((idx for idx, num in enumerate(num_list) if num < 0), -1)

    # next : 값을 첫번 째 요소 하나만 반환 , 뒤에는 값이 없을 때 출력할 값



'''
def solution(num_list):
    return ([i for i in range(len(num_list)) if num_list[i] < 0] or [-1])[0]
'''