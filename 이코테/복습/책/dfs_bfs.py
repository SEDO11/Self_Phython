#dfs

from collections import deque
import sys
input = sys.stdin.readline
def dfs(v):
    vd[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not vd[i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    vb[v] = True
    print(v, end=' ')
    while q:
        p = q.popleft()
        for i in graph[p]:
            if not vb[i]:
                print(i, end=' ')
                vb[i] = True
                q.append(i)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
vd = [False] * (n+1)
vb = [False] * (n+1)

for i in range(n+1):
    graph[i].sort()

dfs(v)
print()
bfs(v)