# 성적 통계

k = int(input())
cnt = 1
for i in range(k):
    n = list(map(int, input().split()))
    n2 = []
    for j in range(1, len(n)):
        n2.append(n[j])
    n2.sort(reverse=True)
    maxi = n2[0]
    mini = n2[len(n2)-1]
    gap = n2[0] - n2[1]
    for j in range(1, len(n2)-1):
        if n2[j]-n2[j+1] > gap:
            gap = n2[j] - n2[j+1]
    print("Class {}\nMax {}, Min {}, Largest gap {}".format(cnt, maxi, mini, gap))
    cnt += 1