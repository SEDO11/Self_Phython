#보너스 점수

n = int(input())
s = input()
cnt, result = 0, 0
for i in range(n):
    if s[i] == "O":
        if i > 0 and s[i] == s[i-1]:
            cnt += 1
            result += cnt
        result += i+1
    else:
        cnt = 0
print(result)