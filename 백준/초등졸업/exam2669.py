#직사각형 네개의 합집합의 면적 구하기

list_xy = []
cnt = 0

while cnt < 4: # 4번 반복
    x1, y1, x2, y2 = list(map(int, input().split()))
    
    for i in range(x1, x2): # 각 좌표 마다 리스트에 저장
        for j in range(y1, y2):
            list_xy.append([i, j])
    cnt += 1
    
list_area = [] # 면적 저장 리스트
for v in list_xy : # 같은 값이 있는경우 저장하지 않음
    if v not in list_area:
        list_area.append(v)
print(len(list(list_area))) # 면적의 개수 출력