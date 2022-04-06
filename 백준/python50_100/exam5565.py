#영수증

total = int(input())
cnt = 0
while cnt < 9:
    a = int(input())
    if total >= a:
        total -= a
        cnt += 1
print(total)