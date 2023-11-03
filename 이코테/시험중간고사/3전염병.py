#전염병

def dfs(x, y):
    if 0<=x<n and 0<=y<m and graph[x][y] == 1:
        graph[x][y] = 0
        print('[{}, {}]'.format(x, y), end=' ')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

n = 4
m = 5
cnt = 0
x, y, k =0, 0, 0
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    graph.append(list(map(int, input())))

print('{', end='')
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            print(str(k) + ':', end=' ')
            print('[', end='')
            dfs(i, j)
            cnt += 1
            k += 1
            print(']', end='')
            print(',', end=' ')
print('}', end='')