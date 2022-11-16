#최대 이익
print('n:', end=' ')
n = int(input())
print('list of price:', end=' ')
l = list(map(int, input().split()))
r = 0
for i in range(1, len(l)):
    if l[i-1] < l[i]:
        r += l[i] - l[i-1]

print('max profit: {}'.format(r))