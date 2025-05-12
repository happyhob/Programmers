'''
정수 배열 arr과 delete_list가 있습니다. 
arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은 원소들은 기존의 arr에 있던 
순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요.
'''

# def solution(arr, delete_list):
#     return list(set(arr)-set(delete_list))


def solution(arr, delete_list):
    temp =[]
    for a in arr:
        if a not in delete_list:
            temp.append(a)
            
    return temp

'''
def solution(arr, delete_list):

    return [i for i in arr if i not in delete_list]
'''

'''
def solution(arr, delete_list):
    answer = []
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr
'''
