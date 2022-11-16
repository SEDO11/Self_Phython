#이진탐색 

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

n, k = map(int, input().split())
l = list(map(int, input().split()))
index = len(l)//2

r = binary_search(l, k, 0, n-1)
if r == None:
    print('None')
else:
    print(r+1)