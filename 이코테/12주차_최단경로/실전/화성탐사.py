# 입력값이 작아서 플로이드 워셜을 쓰는걸로 생각하기 쉽지만
# N의 범위를 봤을 때 최대 125이나 이 문제는 2차원 배열로
# 들어오기 때문에 전체 노드 개수는 125 * 125개로 10000개 이상이 넘어간다. 
# 그러므로 플로이드 워셜 알고리즘은 사용해선 안된다
# 최단경로 알고리즘을 통해 연산해야 한다.

# import heapq

# for _ in range(int(input())):
#     n = int(input())
#     INF = int(1e9)
#     graph = []
#     for _ in range(n):
#         graph.append(list(map(int, input().split())))
#     distance = [[INF] * n for _ in range(n)]

#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]

#     q = []
#     heapq.heappush(q, (graph[0][0], 0, 0))  # cost, x, y
#     distance[0][0] = graph[0][0]
#     while q:
#         dist, x, y = heapq.heappop(q)
#         if dist > distance[x][y]:
#             continue
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             cost = dist + graph[nx][ny]
#             if cost < distance[nx][ny]:
#                 distance[nx][ny] = cost
#                 heapq.heappush(q, (cost, nx, ny))  # 갱신된 거리값을 넣어야지!

#     print(distance[n-1][n-1])

print(1000000//10*15)