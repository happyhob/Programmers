'''
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
'''

str = input()
newstr = ''
for s in str:
    if s.islower():
        newstr +=s.upper()
    else:
        newstr +=s.lower()

print(newstr)

'''
print(input().swapcase())
'''

'''
print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))
'''
