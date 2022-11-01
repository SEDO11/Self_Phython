#음료수 얼려먹기

import sys
sys.setrecursionlimit(10**9)

def dfs(a, b):
    if 0<=a<m and 0<=b<n:
        if graph[a][b] == 1:
            graph[a][b] = 0
            for i in range(8):
                dfs(a+dx[i],b+dy[i])

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    cnt = 0
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = []
    for _ in range(m):
        graph.append(list(map(int, input().split())))
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)