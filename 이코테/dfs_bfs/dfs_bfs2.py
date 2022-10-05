# dfs, bfs

from collections import deque

def dfs(graph, s, v):
    v[s] = True
    print(s, end=' ')
    for i in graph[s]:
        if v[i] == False:
            dfs(graph, i, v)

def bfs(graph, s, v):
    q = deque([s])
    v[s] = True
    while q:
        value = q.popleft()
        print(value, end=' ')
        for i in graph[value]:
            if v[i] == False:
                q.append(i)
                v[i] = True

n, m, s = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, len(graph)):
    graph[i].sort()

v = [False] * (n+1)
dfs(graph, s, v)
print()
v = [False] * (n+1)
bfs(graph, s, v)