# 최단경로(다익스트라) 알고리즘 구현
# 노드의 개수가 5000개 이하라면 실행 가능
# 5000를 초과하면 실행 불가

import sys
input = sys.stdin.readline
inf = int(10e9)

# 노드 수, 간선 수 입력
n, m = map(int, input().split())

# 시작노드 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n+1)]

# 방문한 적이 있는지 체크하는 목적의 리스트 생성
visited = [False] * (n+1)

# 최단 거리  테이블을 모두 무한으로 초기화
distance = [inf] * (n+1)

#모든 간선 정보 입력
for _ in range(m):
    # a 에서 b로 가는데 걸리는 시간(c)
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서. 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = inf
    index = 0 # 최단거리가 가장 짧은 노드의 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:  # type: ignore
            min_value = distance[i]
            index = i
    return index


# 최단경로 알고리즘
def dijkstra(start):
    # 시작노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # 연결된 노드에 걸리는 시간을 입력
    
    # 시작 노드를 제외한 전체  n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

# 출력
for i in range(1, n+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])
