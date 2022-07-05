#dfs

# def dfs(v, r, e):
#     e[r] = True
#     print(r)
    
#     for i in v[r]:
#         if not e[i]:
#             dfs(v, r, e)

# v, e, r = map(int, input().split())
# g = [[] * x for x in range(v+1)]
# x = [False] * (v+1)

# for i in range(e):
#     a, b = map(int, input().split())
#     g[a].append(b)
#     g[b].append(a)
    
# for i in range(1, e+1):
#     g[i].sort()
    
# dfs(g, r, x)

#dfs_bfs

def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v) 
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            return dfs(graph, i, visited)
                
n, m, v = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1): # 순차 정렬
    graph[i].sort()

visitedDfs = [False] * (n+1)

dfs(graph, v, visitedDfs)