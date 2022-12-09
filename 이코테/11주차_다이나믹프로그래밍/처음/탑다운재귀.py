# 탑다운 다이나믹 프로그래밍 재귀 방식
# 내가 많이 쓰는 방식(for)이랑 별 차이는 없네
import time

d = [0] * 100
start_time = time.time()
def fibo(x):
    
    if x==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(99))
end_time = time.time()
print(end_time-start_time)