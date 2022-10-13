# 문자열 압축

def solution(s):
    answer = 1000
    for i in range(1, len(s)):
        r = ''
        cnt = 1
        c = s[:i]
        for j in range(i, len(s)+i, i):
            if s[j:i+j] == c:
                cnt += 1
            else:
                if cnt > 1:
                    r += str(cnt) + c
                else:
                    r += c
                cnt = 1
                c = s[j:i+j]
        answer = min(answer, len(r))
    return answer

s = input()
print(solution(s))