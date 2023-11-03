#dfs 중복 조합 그래프 탐색

candidates = [2, 3, 6, 7]
target = 7
result = []

def dfs(csum, index, path):
    #종료
    if csum < 0: # target을 못 찾은 경우
        return
    if csum == 0: # target을 찾은 경우
        result.append(path)
        return
    
    # 자신부터 하위 원소 까지의 나열 재귀호출
    for i in range(index, len(candidates)):
        dfs(csum - candidates[i], i, path + [candidates[i]])

dfs(target, 0, [])
print(result)