# 저울
# 젤 수 없는 무게 출력

n = input()
k = list(map(int, input().split()))
k.sort()
t = 1
for i in k:
    if i > t:
        break
    t += i
print(t)