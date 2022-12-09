n = int(input())
l = []
l = list(map(int, input().split()))
l.sort()
print(l[(n-1)//2])