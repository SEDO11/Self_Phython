#이진탐색

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

l = [3, 1, 19, 7, 13, 11, 9, 17, 15, 5]
l.sort()

print('찾으려는 수 입력: ', end=' ')
t = int(input())

r = binary_search(l, t, 0, len(l)-1)
if r == None:
    print('입력한 값을 찾을 수 없음')
else:
    print(r+1)

