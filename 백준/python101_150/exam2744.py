#대소문자 바꾸기

#내가 쓴 코드
s = input()
r = ""
for i in s:
    if i.isupper():
        r += i.lower()
    else:
        r += i.upper()
print(r)

# swapcase는 대문자를 소문자로 소문자를 대문자로 바꿔준다.
s = input()
print(s.swapcase())