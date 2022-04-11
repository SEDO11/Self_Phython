# 더하기
# t는 테스트 케이스 개수
# n은 숫자 개수

t = int(input())
for _ in range(t):
    n = int(input())
    list_n = list(map(int, input().split()))
    print(sum(list_n))