#부분집합

nums = [1, 2, 3]
result = []

def dfs(index, path):
    #매 번 결과 추가
    result.append(path)
    
    # 경로를 만들면서 dfs
    for i in range(index, len(nums)):
        dfs(i+1, path + [nums[i]])

dfs(0, [])
print(result)