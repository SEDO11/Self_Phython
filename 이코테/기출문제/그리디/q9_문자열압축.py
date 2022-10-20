#문자열 압축

#프로그래머스 제출용 코드
def solution(s):
    min_r = 1000
    for i in range(1, len(s)+1):
        c = s[:i]
        cnt = 1
        r = ''
        for j in range(i, len(s)+i, i):
            if c == s[j:i+j]:
                cnt += 1
            else:
                if cnt > 1:
                    r += str(cnt) + c
                else:
                    r += c
                c = s[j:i+j]
                cnt = 1
        min_r = min(len(r), min_r)
    return min_r

#내가 짠 코드
s = input()
min_r = 1000
for i in range(1, len(s)+1): # 입력된 문자열의 길이가 1인 경우를 위해 len(s)+1
    c = s[:i]
    cnt = 1
    r = ''
    for j in range(i, len(s)+i, i):
        if c == s[j:i+j]:
            cnt += 1
        else:
            if cnt > 1:
                r += str(cnt) + c
            else:
                r += c
            c = s[j:i+j]
            cnt = 1
    min_r = min(len(r), min_r)
print(min_r)