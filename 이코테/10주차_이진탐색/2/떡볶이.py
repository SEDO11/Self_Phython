def bs(arr, target, start, end):
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
        return bs(arr, target, mid+1, end)
    elif result < target:
        return bs(arr, target, start, mid-1)
    
n, k = map(int, input().split())
l = list(map(int, input().split()))
maxi = max(l)

r = bs(l, k, 0, maxi)
if r == None:
    print('None')
else:
    print(r)