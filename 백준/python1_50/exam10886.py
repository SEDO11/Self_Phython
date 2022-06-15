# 귀여운지 안 귀여운지

run = int(input())

c = 0
n = 0

for i in range(run):
    cute = int(input())
    if cute == 1:
        c += 1
    else :
        n += 1

if c > n:
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")