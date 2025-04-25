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