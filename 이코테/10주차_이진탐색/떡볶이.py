#떡볶이 떡 만들기

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    result = 0
    for i in arr:
        if i > mid:
            result += i - mid
    
    if result == target:
        return mid
    elif result > target:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1)

n, k = map(int, input().split())
l = list(map(int, input().split()))
maxi = max(l)

r = binary_search(l, k, 0, maxi)
if r == None:
    print('None')
else:
    print(r)