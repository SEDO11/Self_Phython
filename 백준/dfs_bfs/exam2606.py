#바이러스 dfs

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return visited.count(True) - 1

r = int(input())
graph = [[] * x for x in range(r+1)]
t = int(input())
visited = [False] * (r+1)

for _ in range(t):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(dfs(graph, 1, visited))