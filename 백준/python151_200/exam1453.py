#피시방 알바

t = int(input())
l = list(map(str, input().split()))
k = []
cnt = 0
for i in l: 
    if i not in k:
        k.append(i)
    else:
        cnt += 1
print(cnt)
