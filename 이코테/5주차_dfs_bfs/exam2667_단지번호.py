# 단지번호 붙이기
# dfs

def dfs(x, y):
    global cnt
    if x < 0 or y < 0 or x >= n or y >= n:
        pass
    else:
        if graph[x][y] == 1:
            cnt += 1
            graph[x][y] = 0
            for i in range(4):
                dfs(x + dx[i], y + dy[i])

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 지도 리스트
graph = []

# 결과값 리스트
l = [] 

# 반복 횟수, 지도 크기 입력
n = int(input())

# 지도 입력
for _ in range(n):
    graph.append(list(map(int, input())))

# for문을 이용한 dfs 연산
cnt = 0
for i in range(n):
    for j in range(n):
        dfs(i, j)
        if cnt > 0:
            l.append(cnt)
            cnt = 0

# 출력
print(len(l))
l.sort()
for i in l:
    print(i)