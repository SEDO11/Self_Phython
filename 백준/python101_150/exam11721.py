# 열 개씩 끊어 출력하기

s = input()
for i in range(len(s)):
    print(s[i], end='')
    if i%10 == 9:
        print()