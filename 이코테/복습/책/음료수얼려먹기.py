#음료수 얼려먹기

def dfs(a, b):
    if 0<=a<n and 0<=b<m:
        if graph[a][b] == 0:
            graph[a][b] = 1
            for i in range(4):
                dfs(a+dx[i],b+dy[i])

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)