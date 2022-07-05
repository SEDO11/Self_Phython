#dfs_bfs

from collections import deque as d

def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
                   
def bfs(graph, v, visited):
     # 큐 구현을 위해 deque 라이브러리 사용
    q = d([v])
    # 현재 노드를 방문 처리
    visited[v] = True
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = q.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
n, m, v = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1): # 순차 정렬
    graph[i].sort()

visitedDfs = [False] * (n+1)
visitedBfs = [False] * (n+1)

dfs(graph, v, visitedDfs)
print()
bfs(graph, v, visitedBfs)