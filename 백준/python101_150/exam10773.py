# 제로
# 자료구조, 스택

t = int(input())
l = []
for _ in range(t):
    n = int(input())
    if n != 0:
        l.append(n)
    else:
        del l[-1]
print(sum(l))