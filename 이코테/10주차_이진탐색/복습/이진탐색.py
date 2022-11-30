# 이진 탐색

n, t = map(int, input().split())
arr = list(map(int, input().split()))
def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid+1
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return '값을 찾을 수 없습니다.'

result = binary_search(arr, 0, n, t)

print(result)