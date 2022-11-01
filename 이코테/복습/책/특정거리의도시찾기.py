# 특정거리의 도시찾기

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    q = deque([x])
    d[x] = True
    while q:
        p = q.popleft()
        for i in graph[p]:
            if not d[i]:
                v[i] = v[p] + 1
                d[i] = True
                q.append(i)
r = []
n, m, k, x = map(int, input().split())
v = [0] * (n+1)
d = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
for i in range(n+1):
    graph[i].sort()

bfs(x)
for i in range(len(v)):
    if k == v[i]:
        r.append(i)
if len(r) == 0:
    r.append(-1)
r.sort()
for i in r:
    print(i)