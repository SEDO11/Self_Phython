#성적이 낮은 순으로 학생 출력

n = int(input())
l = []
for _ in range(n):
    a, b = map(str, input().split())
    l.append((a, int(b)))

l.sort(key=lambda x: x[1])

for x, y in l:
    print(x, end=' ')
