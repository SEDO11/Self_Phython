#최대이익

r = 0

print('n:', end=' ')
n = int(input())

print('n:', end=' ')
price = list(map(int, input().split()))

for i in range(1, len(price)):
    if price[i-1] < price[i]:
        r += price[i] - price[i-1]

print('max profit: {}'.format(r))