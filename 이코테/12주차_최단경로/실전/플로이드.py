INF = int(1e9)

n = int(input())
m = int(input())
# 2차원 리스트 생성
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    graph[a][a] = 0

# 초기 도시사이의 비용 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c) # 현재 값과 새로 들어온 값 중에 작은 값을 대입

# 다른 도시를 들르고 갈 경우의 비용과 비교
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 도시 사이의 값 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("0", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()