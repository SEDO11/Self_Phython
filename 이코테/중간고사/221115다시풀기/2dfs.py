#dfs

def dfs(start, arr):
    print(start, end=' ')
    v[start] = True
    for i in arr[start]:
        if v[i] == False:
            dfs(i, arr)

graph = [[],
         [2, 3],
         [1, 6, 8],
         [1, 4, 5],
         [3],
         [3],
         [2, 7],
         [6, 8],
         [2, 7]]
v = [False] * 9
dfs(1, graph)