#입력된 것에서 모든 알파벳을 오름차순으로 정렬하고 뒤에 모든 숫자를 더한 값을 추출

import time

# filter 사용
a = input()
b = list(filter(str.isalpha, a))
b.sort()
b =''.join(b)
cnt = len(list(filter(str.isdigit, a)))
c = str(sum(list(map(int, filter(str.isdigit, a)))))
print(b+(c if cnt > 0 else '')) # 숫자가 입력되지 않으면 출력하지 않음

# filter 사용 x
s = input()
a = []
n = 0
cnt = 0
for i in s:
    if i.isdigit():
        n += int(i)
        cnt += 1
    else:
        a.append(i)
a.sort()
print(''.join(a)+str(n if cnt > 0 else '')) # 숫자가 입력되지 않으면 출력하지 않음