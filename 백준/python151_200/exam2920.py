#음계

# 내가 작성한 코드
l = list(map(int, input().split()))
r = ""
if l[0] > l[7]:
    for i in range(len(l) -1):
        if(l[i] > l[i+1]):
            r = "descending"
        else:
            r = "mixed"
            break
else:
    for i in range(len(l) -1):
        if(l[i] < l[i+1]):
            r = "ascending"
        else:
            r = "mixed"
            break
print(r)

# 다른 사람이 작성한 코드
s = input().replace(' ', '')
if s == "12345678":
    r = "ascending"
elif s == "87654321":
    r = "descending"
else:
    r = "mixed"
print(r)