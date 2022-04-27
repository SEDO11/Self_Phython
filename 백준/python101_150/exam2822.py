# 점수 계산

list_n,cnt = [], []
result,cnt_r = 0, ""
for i in range(8):
    list_n.append([int(input()), i+1])
list_n.sort()
for i in range(3, len(list_n)):
    result += list_n[i][0]
    cnt.append(list_n[i][1])
cnt.sort()
for i in cnt:
    cnt_r += str(i) + " "
print(result)
print(cnt_r)

#sorted 함수 이용
# list_n,cnt = [], []
# for i in range(8):
#     list_n.append(int(input()))
# list_a = sorted(list_n)
# for i in cnt:
#     cnt_r += str(i) + " "
# print(result)
# print(cnt_r)