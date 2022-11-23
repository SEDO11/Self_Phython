#플로이드

import math

n = int(input())
m = int(input())
INF = math.inf
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    graph[a][a] = 0

# 주어진 시작,도착 도시, 비용 graph에 반영 -> 시작->도착 도시 연결하는 노선 여러개일 수 있음에 주의!
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = min(graph[a][b], cost)

# 거쳐가는 노드 k로 탐색하면서 플로이드워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()