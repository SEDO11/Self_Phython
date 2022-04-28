#짝수 찾기

#정답
t = int(input())
for i in range(t):
    n = []
    l = list(map(int, input().split()))
    for j in l:
        if j % 2 == 0:
            n.append(j)
    print(sum(n), min(n))

#내가쓴 코드 정답 처리 안해줌...
# t = int(input())
# for i in range(t):
#     l = list(map(int, input().split()))
#     for j in l:
#         if j % 2 != 0:
#             l.remove(j)
#     print(sum(l), min(l))