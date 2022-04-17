# 평범한 배낭
import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
list_wv = []
result_w = 0
result_v = 0
for _ in range(n):
    list_wv.append(list(map(int, input().split())))
list_wv.sort(key=lambda x: (x[0], -x[1])) #첫번째 인덱스 오름차순, 두 번째 인덱스 내림차순
for i in range(n):
    result_w += int(list_wv[i][0])
    if result_w > k:
        break
    else :
        result_v += int(list_wv[i][1])
print(result_v)