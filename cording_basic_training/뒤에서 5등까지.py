def solution(num_list):
    answer = []
    for i in range(0,5):
        min_value = min(num_list)
        answer.append(min_value)
        num_list.remove(min_value)
    return answer


### sorted 오름차순 정리
### 오름차수 정리된 리스트의 index =4까지만 출력하면 됨
'''
def solution(num_list):
    return sorted(num_list)[:5]
'''