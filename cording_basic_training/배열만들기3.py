'''
정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.

intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은 닫힌 구간입니다. 닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.

이때 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.
'''

def solution(arr, intervals):
    temp = [arr[interval[0]:interval[1]+1] for interval in intervals]
    return [e for t in temp for e in t]


'''
def solution(arr, intervals):
    s1, e1 = intervals[0]
    s2, e2 = intervals[1]
    return arr[s1:e1+1] + arr[s2:e2+1]
'''


'''
def solution(arr, intervals):
    answer = []
    for a,b in intervals: answer+=arr[a:b+1]
    return answer

'''