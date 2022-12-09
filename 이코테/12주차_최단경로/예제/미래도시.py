#미래도시, 입력값의 범위가 작으므로 플로이드 워셜을 이용

INF = int(1e9)

n, m = map(int, input().split())
# 2차원 리스트 생성
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
x, y = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][y] + graph[y][x]

if distance >= INF:
    print('-1')
else:
    print(distance)