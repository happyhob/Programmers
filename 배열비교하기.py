'''
 두배열이 길이가 다름
    > 두 배열의 합 비교

 
 arr2> arr1   : -1
 arr2 <arr1   : 1
 arr2 = arr2  : 0
'''


def solution(arr1, arr2):
    arr1_len, arr2_len = len(arr1), len(arr2)
    
    if arr2_len > arr1_len:
        return -1
    elif arr2_len < arr1_len:
        return 1
    else:
        arr1_sum , arr2_sum = sum(arr1), sum(arr2)
        if arr2_sum > arr1_sum: return -1
        elif arr2_sum < arr1_sum: return 1
        else: return 0
    

'''
def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))

'''