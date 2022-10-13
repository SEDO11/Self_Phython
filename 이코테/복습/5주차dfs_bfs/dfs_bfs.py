#dfs, bfs 구현

from collections import deque

def dfs(s):
    if n >= s >= 1:
        dv[s] = True
        print(s, end=' ')
        for i in graph[s]:
            if not dv[i]:
                dfs(i)

def bfs(s):
    q = deque([s])
    
    while q:
        x = q.popleft()
        if not bv[x]:
            bv[x] = True
            print(x, end=' ')
            for i in graph[x]:
                q.append(i)

n, m, s = map(int, input().split())
graph = [[] for _ in range(n+1)]
dv = [False] * (n+1)
bv = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1):
    graph[i].sort()
    
dfs(s)
print()
bfs(s)