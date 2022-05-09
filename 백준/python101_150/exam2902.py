# kmp 알고리즘
# 첫번째 대문자만으로 글자를 만들어 출력

s = input()
r = ""
for i in s:
    if i.isupper():
        r += i
print(r)