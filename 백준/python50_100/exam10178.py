#할로윈 사탕
import sys
input = sys.stdin.readline

run = int(input())
for _ in range(run):
    c, v = map(int, input().split())
    r1 = c // v
    r2 = c % v
    print("You get", r1,"piece(s) and your dad gets", r2,"piece(s).")