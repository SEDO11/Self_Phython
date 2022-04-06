#남은 사과 총 합

run = int(input())
result = 0
for i in range(run):
    s, a = map(int, input().split())
    result += a % s
print(result)