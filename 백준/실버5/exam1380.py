#귀걸이

import sys
input = sys.stdin.readline
result = []
r = 0

while True:
    t = int(input())
    if t == 0:
        break
    students = []
    earing = []
    for _ in range(t): # 학생 
        students.append(input().strip())
        
    for _ in range((t*2)-1): # 귀걸이 목록
        s = list(map(str, input().split()))
        if len(s) == 2:
            earing.append(int(s[0]))
            
    for i in range(1, t+1): # 귀걸이를 못 받은 인원 저장
        if earing.count(i) != 2:
            result.append(students[i-1])
            
    print(r+1, result[r])
    r += 1