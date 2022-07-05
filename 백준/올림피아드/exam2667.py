#단지번호 붙이기

#dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >=n:
        return False
    if graph[x][y] == 1:
        global c
        c += 1
        #해당노드 방문처리
        graph[x][y] = 0
        #상하좌우의 위치들도 모두 재귀적으로 호출
        #여기에서 주변에 붙어있는 모든 0에 속한 값들을 1로 변환
        #그래서 처음에 나온 0값만 셈
        dfs(x-1, y) # 좌
        dfs(x, y-1) # 상
        dfs(x+1, y) # 우
        dfs(x, y+1) # 하
        return True # 현재 입력된 값이 0인 경우 True 리턴
    return False

n = int(input())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드에 대하여 음료수 채우기
result = 0
c = 0
l = []
for i in range(n):
    for j in range(n):
        #현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            l.append(c)
            result += 1
            c = 0

print(result) # 정답 출력
l.sort()
for i in l:
    print(i)