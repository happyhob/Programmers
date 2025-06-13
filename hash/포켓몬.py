'''
n마리 중 n/2 만큼 가져갈 수 있음

종류에 따라 번호룰 붙여 구분 ( 같은 종류의 포켓몬은 같은 번호를 가짐)


n개에서 r개를 뽑아서 선택할 수 있는 조합

n! / r!(n-r)!

최대한 많은 종류의 포켓몬을 가지기를 원함!!
    
n개 중에서
n//2를 뽑을 때 , 최대한 중복이 없기 뽑기!

'''
def permute(arr,r):
    result =set()
    visited = [False] *len(arr)
    
    def backtrack(path):
        if len(path)==r:
            result.add(tuple(path))
            return
        
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] =True
                path.append(arr[i])
                backtrack(path)
                path.pop()
                visited[i] = False
    backtrack([])
    return result
def solution(nums):
    max = 0
    comb = permute(nums,len(nums)//2)
    
    for p in comb:
        if len(set(p))> max:
            max = len(set(p))
            
    return max

#위의 코드는 전체의 조합을 다루고 있는 코드로 잤는데, 문제 해결은 가능하겠지만 runtime error가 났다.

def solution(nums):
    r = len(nums)//2
    not_overlap = set(nums)
    
    if len(not_overlap) >= r:
        return r
    
    else:
        return len(not_overlap)
    
# 문제를 읽고 다시 생각을 했더니 정말 간단한 코드가 나왔다..
