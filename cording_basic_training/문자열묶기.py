'''
문자열 배열 strArr이 주어집니다. strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.
'''

def solution(strArr):

    s_dit ={}
    for i,s in enumerate(strArr):
        if len(s) in s_dit:
            s_dit[len(s)] +=1
        else:
            s_dit[len(s)]=1
    
    max_value = max(s_dit.values())
    result_key=0
    for key,value in s_dit.items():
        if value==max_value and result_key <key:
            result_key = key
            
    return s_dit[result_key]
            
            
  '''
  def solution(strArr):
    a=[0]*31
    for x in strArr: a[len(x)]+=1
    return max(a)
  '''


'''
def solution(strArr):
    d = {}

    for i in strArr:
        d[len(i)] = d.get(len(i), 0) + 1

    return max(d.values())
'''

'''
def solution(strArr):
    w_len = [0 for _ in range(31)]
    for w in strArr:
        w_len[len(w)] += 1
    return max(w_len)
'''
