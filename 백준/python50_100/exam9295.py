#주사위
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    d1, d2 = map(int, input().split())
    print("Case "+str(i+1)+":", d1+d2)