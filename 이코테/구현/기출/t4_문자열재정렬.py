#입력된 것에서 모든 알파벳을 오름차순으로 정렬하고 뒤에 모든 숫자를 더한 값을 추출

import time

a = input()
stime = time.time()
b = list(filter(str.isalpha, a))
b.sort()
b =''.join(b)
c = str(sum(list(map(int, list(filter(str.isdigit, a))))))
print(b+c)
etime = time.time()
print(etime-stime)