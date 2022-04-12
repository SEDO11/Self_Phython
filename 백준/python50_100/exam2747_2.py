# 피보나치 수, 재귀 함수 이용
# 이걸로 제출하면 시간이 초과된다.

def fn(num):
    if num == 0: return 0
    elif num == 1: return 1
    else: return fn(num-1) + fn(num-2)
n = int(input())
print(fn(n))