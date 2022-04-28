#소트인사이드

# 내가 작성한 코드
# a = input()
# list_a = []
# result = ""
# for i in range(len(a)):
#     list_a.append(int(a[i]))
# list_a.sort(reverse=True)
# for i in  range(len(a)):
#     result += str(list_a[i])
# print(result)

# 실용적인 코드
a = list(map(int,input()))
a.sort(reverse=True)
for i in a:
    print(i, end="")