'''
랜덤으로 서로 다른 k개의 수를 저장한 배열을 만드려고 합니다. 적절한 방법이 떠오르지 않기 때문에 일정한 범위 내에서 무작위로 수를 뽑은 후, 지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가하는 방식으로 만들기로 합니다.

이미 어떤 수가 무작위로 주어질지 알고 있다고 가정하고, 실제 만들어질 길이 k의 배열을 예상해봅시다.

정수 배열 arr가 주어집니다. 문제에서의 무작위의 수는 arr에 저장된 순서대로 주어질 예정이라고 했을 때, 완성될 배열을 return 하는 solution 함수를 완성해 주세요.

단, 완성될 배열의 길이가 k보다 작으면 나머지 값을 전부 -1로 채워서 return 합니다.
'''

def solution(arr, k):
    new_arr = list(dict.fromkeys(arr))
    if len(new_arr)<k:
        for i in range(k-len(new_arr)):
            new_arr.append(-1)
        return new_arr[:k]
    
    elif len(new_arr)>=k:
        return new_arr[:k]


'''
def solution(arr, k):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
        if len(ret) == k:
            break

    return ret + [-1] * (k - len(ret))
'''

'''
def solution(arr, k):
    res = list(dict.fromkeys(arr))
    res.extend([-1] * max(0, k - len(res)))
    return res[:k]
'''
