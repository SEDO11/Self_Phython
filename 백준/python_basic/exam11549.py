# 차 맞추기

correct = int(input()) # 정답
list_answer = map(int, input().split())
cnt = 0
for i in list_answer:
    if i == correct:
        cnt += 1
print(cnt)