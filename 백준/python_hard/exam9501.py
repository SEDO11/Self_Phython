# 꿍의 우주 여행

run = int(input())

for i in range(run):
    result = 0
    n, d = map(int, input().split()) # 우주선의 개수n, 목적지까지의 거리 d
    for j in range(n):
        v, f, c = map(int, input().split()) # 우주선의 최고속도 v, 연료양 f, 연료소비율 c
        if (f / c) * v >= d:
            result += 1         
    print(result)