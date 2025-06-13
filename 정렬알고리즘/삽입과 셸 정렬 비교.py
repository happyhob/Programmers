'''
삽입 정렬은 gap이 1로 고정된 쉘 정렬이라고 봐도 좋다.

셸 정렬은 삽입 정렬을 조금 강화한 알고리즘 이다.
gap을 계속 2로 나누어 가며, gap만큼을 비교하며 정렬하는 알고리즘이다.
결국 마지막에는 gap이 1이되고, 삽입 정렬과 같은 기능을 수행하게 된다.!!

그럼 왜 셸 정렬을 사용할까?
삽입 정렬을 정렬이 어느 정도 되어 있을 때, 정렬의 효율이 늘어난다.
그래서 gap만큼으로 먼저 비교를 해가며 어느 정도 정렬을 하고, 삽입 정렬을 수행하게 되면, 효율이 증가하게 된다.

일반적인 삽입 정렬보다 훨씬 적은 이동으로 정렬이 끝날 수 있는 것
'''

#삽입정렬
def inserted_sort(arr):
  n = len(arr)
  for i in range(1,n):
    j = i-1
    temp = arr[i]

    while j>=0 and arr[j]> temp:
      arr[j+1] = arr[j] 
      j-=1
    arr[j+1] = temp
  return arr
  
#셸정렬
def shell_sort(arr):
  n = len(arr)
  gap = n//2

  while gap >0:
    for i in range(gap, n):
      temp = arr[i]
      j = i
      while j>=gap and arr[j-gap]>temp:
        arr[j]= arr[j-gap]
        j-= gap
      arr[j]  = temp;

    gap//=2 
  return arr
 
arr2 = [3,2,5,4,6,1]
shell_sort(arr2)
# inserted_sort(arr2)
