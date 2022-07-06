# 평범한 배낭
import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
table = [0] * (k+1) # 최대 무게 범위 만큼 리스트  생성
for _ in range(n): 
    w, v = map(int, input().split())
    for j in range(k, 0, -1):
        if j + w <= k and table[j] != 0: # 무게를 더했을 때 7 이하면서 가치가 0이 아니면 합친다.
            table[j+w] = max(table[j+w], table[j] + v)           
    if w <= k:
        table[w] = max(table[w], v) # table[w] == 0
print(max(table))