#미로 탈출

from collections import deque

def bfs(a, b):
    global graph
    q = deque()
    q.append((a, b))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0>nx or nx >= n or ny >= m or ny < 0:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                q.append((nx, ny))

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0, 0)
print(graph[n-1][m-1])
