#인공지능 시계

hms = input().split()
timer = int(input())

h = int(hms[0])
m = int(hms[1])
s = int(hms[2])

fs = 60 #60초 1분, 60분 1시간
fh = 24

s += int(timer % fs)
m += int(timer / fs)

if s > 59:
    m += int(s / fs)
    s = int(s % fs)
if m > 59:
    h += int(m / fs)
    m = int(m % fs)
if h > 23:
    h = int(h % fh)
    
print(h, m, s)