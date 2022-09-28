# 문자열 압축

def solution(s):
    answer = 1000
    for i in range(1, len(s)+1):
        r = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s)+i, i):
            if s[j:i+j] == tmp:
                cnt += 1
            else:
                if cnt > 1:
                    r += str(cnt) + tmp
                else:
                    r += tmp
                tmp = s[j:i+j]
                cnt = 1
        answer = min(answer, len(r))
    return answer

s = input()
print(solution(s))