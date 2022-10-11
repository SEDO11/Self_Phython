#음료수얼려먹기

def dfs(x, y, g):
    if n > x >= 0 and m > y >= 0 and g[x][y] == 0:
        g[x][y] = 1
        dfs(x-1, y, g)
        dfs(x+1, y, g)
        dfs(x, y-1, g)
        dfs(x, y+1, g)

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j, graph)
            cnt += 1
print(cnt)