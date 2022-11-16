#고정점 찾기

def binary_search(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if mid == arr[mid]:
        return mid
    elif mid > arr[mid]:
        return binary_search(arr, mid+1, end)
    else:
        return binary_search(arr, start, mid-1)

n = int(input())
l = list(map(int, input().split()))

r = binary_search(l, 0, n)
if r == None:
    print(-1)
else:
    print(r)