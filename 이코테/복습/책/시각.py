#시각

n = int(input())
cnt = 0
for i in range(1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

if n >= 3:
    cnt *= (n+1)
    cnt += (60 * 60) - 1575
else:
    cnt *= (n+1)
print(cnt)