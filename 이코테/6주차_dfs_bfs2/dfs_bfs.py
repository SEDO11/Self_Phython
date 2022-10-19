#dfs bfs
from collections import deque
import sys
input = sys.stdin.readline

def dfs(s, visit):
    visit[s] = True
    print(s, end=' ')
    for i in graph[s]:
        if not visit[i]:
            dfs(i, visit)

def bfs(s, visit):
    q = deque([s])
    visit[s] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visit[i]:
                visit[i] = True
                q.append(i)

n ,m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

visit = [False] * (n+1)
dfs(v, visit)
print()
visit = [False] * (n+1)
bfs(v, visit)