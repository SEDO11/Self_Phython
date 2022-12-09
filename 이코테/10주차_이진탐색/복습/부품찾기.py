#부품찾기

n1 = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
n2 = int(input())
arr2 = list(map(int, input().split()))

def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return 'yes'
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return 'no'

for i in arr2:
    result = binary_search(arr1, 0, len(arr1), i)
    print(result, end=' ') 