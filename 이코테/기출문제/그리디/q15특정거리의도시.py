#특정 거리의 도시 찾기

from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())

def bfs(x):
    answer = []
    q = deque([x])
    v[x] = True
    cnt[x] = 0
    while q:
        value = q.popleft()
        for i in graph[value]:
            if not v[i]:
                cnt[i] = cnt[value] + 1
                v[i] = True
                q.append(i)
                if cnt[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer

graph = [[] for _ in range(n+1)]
v = [False] * (n+1)
cnt = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in bfs(x):
    print(i)
