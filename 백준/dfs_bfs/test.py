# 파이썬
import sys

def solution(n, lost, reserve):
    t = n - len(lost)
    for i in reserve:
        for j in lost:
            if i-1 == j:
                reserve.remove(i)
                lost.remove(j)
                t += 1
                break
            elif i+1 == j:
                reserve.remove(i)
                lost.remove(j)
                t += 1
                break
    answer = t
    return answer

n = int(sys.stdin.readline())
lost = list(map(int, sys.stdin.readline().split()))
reserve = list(map(int, sys.stdin.readline().split()))
print(solution(n, lost, reserve))
