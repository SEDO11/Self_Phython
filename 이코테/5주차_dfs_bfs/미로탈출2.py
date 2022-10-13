
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            
            if x1 < 0 or y1 < 0 or x1 >= n or y1 >= m:
                continue
            if graph[x1][y1] == 0:
                continue
            if graph[x1][y1] == 1:
                graph[x1][y1] = graph[x][y] + 1
                q.append((x1, y1))
    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

print(bfs(0, 0))