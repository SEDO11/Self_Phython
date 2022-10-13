# 시각

n = int(input())
cnt = 0
# 시간에 3이 
for i in range(1):
    for j in range(60):
        for k in range(60):
            p = str(i) + str(j) + str(k)
            if '3' in p:
                cnt += 1
print(cnt*(n) + 3600 if n >= 3 else cnt*(n+1))