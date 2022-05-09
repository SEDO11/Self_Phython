# 모음의 개수

n = input()
l = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for i in n:
    for j in l:
        if i == j:
            cnt += 1
            break
print(cnt)