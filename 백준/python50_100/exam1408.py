a = list(map(int, input().split(":")))
b = list(map(int, input().split(":")))

sum_a = a[0] * 3600 + a[1] * 60 + a[2]
sum_b = b[0] * 3600 + b[1] * 60 + b[2]
s = sum_b - sum_a
if s < 0:
    s += 60*60*24
m = s // 60
s %= 60
h = m // 60
m %= 60
print("%02d:%02d:%02d" % (h,m,s))