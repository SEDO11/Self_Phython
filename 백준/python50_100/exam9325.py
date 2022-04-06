#얼마

run = int(input()) # 테스트 케이스 개수
for i in range(run):
    s = int(input()) # 자동차 가격
    n = int(input()) # 옵션의 개수
    for j in range(n):
        q, p = map(int, input().split())
        s += q * p
    print(s)