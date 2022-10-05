# dfs bfs

from collections import deque

def dfs(graph, start, v):
    v[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if v[i] == False:
            dfs(graph, i, v)

def bfs(graph, start, v):
    q = deque([start])
    v[start] = True
    while q:
        s = q.popleft()
        print(s, end=' ')
        for i in graph[s]:
            if v[i] == False:
                v[i] = True
                q.append(i)

n, m, s = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

v = [False] * (n+1)
dfs(graph, s, v)
print()
v = [False] * (n+1)
bfs(graph, s, v)