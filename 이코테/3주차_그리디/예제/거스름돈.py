import time
# 거스름돈

# 500, 100, 50, 10
# 거슬러 줘야 할 떄 동전의 최소 개수

m=int(input())
coins = [500, 100, 50, 10]
cnt = 0
s_time = time.time()
for coin in coins:
    cnt += m // coin
    m %= coin
print(cnt)
e_time = time.time()
print(e_time-s_time)