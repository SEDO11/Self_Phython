#음료수 얼려먹기

def dfs(x, y):
    if x >= n or x < 0 or y >= m or y < 0 or graph[x][y] == '1':
        return False
    graph[x][y] = '1'
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    return True

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1
print(cnt)