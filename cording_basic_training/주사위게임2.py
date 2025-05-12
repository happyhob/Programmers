'''
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
'''

def solution(a, b, c):
    if a !=b and b!= c and c!=a:
        return a+b+c
    elif (a==b and a !=c) or (b==c and c!=a) or (c==a and a !=b):
        return (a+b+c)*(a**2+b**2+c**2)
    elif a==b and b==c:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)


''' set()으로 중복을 찾아서 풀이,,, 이건 생각 못
def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)
'''
